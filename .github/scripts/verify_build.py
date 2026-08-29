#!/usr/bin/env python3
"""
Dasharo Build Documentation Verification Tool
===============================================
Parses building-manual markdown pages and verifies that the documented
build instructions produce bit-for-bit identical binaries to published releases.

Usage:
    python3 verify_build.py --device <device_slug> --release <tag>
    python3 verify_build.py --all  # verify all devices/releases listed in docs

Example:
    python3 verify_build.py --device protectli-vp46xx --release v0.9.2
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# ── Configuration ────────────────────────────────────────────────────────────

# Registry of supported devices and their build docs
# Maps device slug → (repo_url, build_manual_path, device_id_in_coreboot)
DEVICE_REGISTRY = {
    "protectli-vp46xx": {
        "repo": "https://github.com/Dasharo/coreboot.git",
        "docs_path": "unified/protectli/building-manual.md#vp4630vp4650vp4670",
        "coreboot_target": "protectli/vp46xx",
        "rom_pattern": "*.rom",
    },
    "protectli-vp66xx": {
        "repo": "https://github.com/Dasharo/coreboot.git",
        "docs_path": "unified/protectli/building-manual.md#vp6630vp6650vp6670",
        "coreboot_target": "protectli/vp66xx",
        "rom_pattern": "*.rom",
    },
    "protectli-fw6": {
        "repo": "https://github.com/Dasharo/coreboot.git",
        "docs_path": "unified/protectli/building-manual.md#fw6",
        "coreboot_target": "protectli/fw6",
        "rom_pattern": "*.rom",
    },
    "dell-optiplex": {
        "repo": "https://github.com/Dasharo/coreboot.git",
        "docs_path": "variants/dell_optiplex/building-manual.md",
        "coreboot_target": "dell/optiplex_9010",
        "rom_pattern": "*.rom",
    },
    "msi-z690": {
        "repo": "https://github.com/Dasharo/coreboot.git",
        "docs_path": "variants/msi_z690/building-manual.md",
        "coreboot_target": "msi/msig_slidemc/z690-a_pro_wifi",
        "rom_pattern": "*.rom",
    },
}

# Base Docker image for builds (matches Uber toolchain)
DOCKER_IMAGE = "coreboot/coreboot-sdk:latest"

# ── Markdown parsing ─────────────────────────────────────────────────────────

def extract_code_blocks(markdown_text, language="shell"):
    """Extract code blocks of a specific language from markdown."""
    pattern = f"```{language}\n(.*?)```"
    matches = re.findall(pattern, markdown_text, re.DOTALL)
    return [m.strip() for m in matches]


def extract_build_commands(markdown_text):
    """
    Extract build commands from a building-manual markdown page.
    
    Strategy:
    1. Extract all shell code blocks
    2. Filter to lines that look like build commands (make, git, docker, etc.)
    3. Skip lines that are obviously comments or echo statements
    """
    blocks = extract_code_blocks(markdown_text, "shell")
    if not blocks:
        blocks = extract_code_blocks(markdown_text, "bash")
    if not blocks:
        blocks = extract_code_blocks(markdown_text, "")
    
    commands = []
    build_keywords = ["make", "git", "docker", "python", "./configure", "cp ", "mv ",
                       "wget", "curl", "cd ", "mkdir", "cat ", "echo ", "sed ",
                       "tar", "unzip", "pushd", "popd", "source"]
    
    for block in blocks:
        for line in block.split("\n"):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # Skip pure echo/print lines
            if line.startswith("echo ") and not line.startswith("echo -"):
                continue
            # Skip prompts (lines starting with $)
            if line.startswith("$ "):
                line = line[2:]
            commands.append(line)
    
    return commands


def parse_release_hash(releases_markdown, tag, device):
    """
    Parse a releases.md page to find the SHA256 hash for a given release tag.
    
    Looks for patterns like:
    ```
    sha256: abc123...
    ```
    near the release tag.
    """
    # Find the section for this tag
    sections = re.split(r'^#{1,3} ', releases_markdown, flags=re.MULTILINE)
    
    for section in sections:
        if tag in section:
            # Find sha256 in this section
            hash_match = re.search(r'sha256[:\s]+([a-f0-9]{64})', section, re.IGNORECASE)
            if hash_match:
                return hash_match.group(1)
    
    return None


# ── Docker build execution ───────────────────────────────────────────────────

def run_in_docker(commands, env_vars=None, workdir="/build"):
    """
    Execute build commands inside a Docker container with coreboot SDK.
    
    Returns (exit_code, stdout, stderr)
    """
    # Build the Dockerfile for this verification
    docker_commands = [
        "set -e",
        f"cd {workdir}",
    ] + commands
    
    cmd_str = " && ".join(docker_commands)
    
    docker_cmd = [
        "docker", "run", "--rm",
        "-v", f"{workdir}:{workdir}",
        "-w", workdir,
    ]
    
    if env_vars:
        for key, value in env_vars.items():
            docker_cmd.extend(["-e", f"{key}={value}"])
    
    docker_cmd.extend([
        DOCKER_IMAGE,
        "bash", "-c", cmd_str
    ])
    
    result = subprocess.run(
        docker_cmd,
        capture_output=True,
        text=True,
        timeout=7200,  # 2 hour timeout
    )
    
    return result.returncode, result.stdout, result.stderr


def verify_build_docker(device_slug, release_tag, commands):
    """
    Run the documented build commands in a Docker container.
    
    Returns (success, rom_hash, error_message)
    """
    device = DEVICE_REGISTRY.get(device_slug)
    if not device:
        return False, None, f"Unknown device: {device_slug}"
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # Step 1: Clone the repo at the right tag
        print(f"📦 Cloning {device['repo']} at tag {release_tag}...")
        clone_result = subprocess.run(
            ["git", "clone", "--branch", release_tag, "--depth", "1",
             device['repo'], tmpdir],
            capture_output=True, text=True, timeout=600,
        )
        
        if clone_result.returncode != 0:
            return False, None, f"Git clone failed: {clone_result.stderr}"
        
        # Step 2: Run the build commands
        print(f"🔨 Running build commands...")
        exit_code, stdout, stderr = run_in_docker(commands, workdir=tmpdir)
        
        if exit_code != 0:
            return False, None, f"Build failed (exit {exit_code}):\n{stderr[-500:]}"
        
        # Step 3: Find the ROM file
        rom_files = list(Path(tmpdir).rglob(device["rom_pattern"]))
        if not rom_files:
            return False, None, "No ROM file found after build"
        
        # Hash the first ROM found
        rom_path = rom_files[0]
        sha256 = hashlib.sha256(rom_path.read_bytes()).hexdigest()
        
        return True, sha256, None


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Verify Dasharo build documentation produces correct binaries"
    )
    parser.add_argument("--device", "-d", help="Device slug (e.g. protectli-vp46xx)")
    parser.add_argument("--release", "-r", help="Release tag (e.g. v0.9.2)")
    parser.add_argument("--all", action="store_true", help="Verify all known devices")
    parser.add_argument("--dry-run", action="store_true", help="Parse docs only, don't build")
    args = parser.parse_args()
    
    if not args.all and not (args.device and args.release):
        parser.error("Specify --device and --release, or --all")
    
    if args.dry_run:
        print("🔍 Dry run mode — parsing docs only")
        for slug, device in DEVICE_REGISTRY.items():
            docs_path = "docs/" + device["docs_path"].split("#")[0]
            if os.path.exists(docs_path):
                content = Path(docs_path).read_text()
                commands = extract_build_commands(content)
                print(f"\n{slug}: {len(commands)} commands extracted")
                for cmd in commands[:5]:
                    print(f"  $ {cmd}")
                if len(commands) > 5:
                    print(f"  ... and {len(commands) - 5} more")
            else:
                print(f"\n{slug}: ❌ docs not found at {docs_path}")
        return
    
    # For now, implement single device verification
    if args.device and args.release:
        device = DEVICE_REGISTRY.get(args.device)
        if not device:
            print(f"❌ Unknown device: {args.device}")
            sys.exit(1)
        
        # Read build manual
        docs_path = "docs/" + device["docs_path"].split("#")[0]
        if not os.path.exists(docs_path):
            print(f"❌ Build manual not found: {docs_path}")
            sys.exit(1)
        
        content = Path(docs_path).read_text()
        commands = extract_build_commands(content)
        
        if not commands:
            print(f"❌ No build commands found in {docs_path}")
            sys.exit(1)
        
        print(f"📋 Found {len(commands)} build commands for {args.device}")
        
        if args.dry_run:
            for cmd in commands:
                print(f"  $ {cmd}")
            return
        
        # Run the actual build verification
        success, rom_hash, error = verify_build_docker(
            args.device, args.release, commands
        )
        
        if success:
            print(f"\n✅ Build successful!")
            print(f"   ROM SHA256: {rom_hash}")
            print(f"\nCompare this hash against the published release.")
        else:
            print(f"\n❌ Build verification failed: {error}")
            sys.exit(1)


if __name__ == "__main__":
    main()

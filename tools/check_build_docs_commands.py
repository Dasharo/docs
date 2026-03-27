#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
# Focus on build docs pages across variants
DOCS = sorted((ROOT / "docs" / "variants").glob("**/building-manual.md"))
BLOCK_RE = re.compile(r"```(?:bash|sh|shell)?\n(.*?)```", re.S)
ALLOWED_PREFIXES = (
    "git ", "make", "cmake", "docker", "podman", "python", "python3", "pip", "pip3",
    "./", "sudo ", "export ", "cd ", "echo ", "cat ", "ls", "mkdir", "rm ", "cp ", "mv ",
    "source ", "ninja", "west", "repo ", "curl ", "wget ", "tar ", "xz ", "unzip ",
)

def extract_blocks(text: str):
    for m in BLOCK_RE.finditer(text):
        b = m.group(1).strip()
        if b:
            yield b

def check_bash_syntax(block: str):
    with tempfile.NamedTemporaryFile("w", suffix=".sh", delete=True) as f:
        f.write(block + "\n")
        f.flush()
        p = subprocess.run(["bash", "-n", f.name], capture_output=True, text=True)
        return p.returncode == 0, (p.stderr or p.stdout).strip()

def is_cmd(line: str):
    s = line.strip()
    if not s or s.startswith("#"):
        return False
    if s in ("fi", "done", "then", "do", "esac", "else"):
        return False
    return True

def main() -> int:
    failures = []
    warns = []
    tested = 0
    if not DOCS:
        print("[docs-check] no build-manual.md files found")
        return 1

    for doc in DOCS:
        text = doc.read_text(encoding="utf-8", errors="ignore")
        for i, block in enumerate(extract_blocks(text), 1):
            tested += 1
            ok, err = check_bash_syntax(block)
            if not ok:
                failures.append((str(doc), i, err))
            for ln, line in enumerate(block.splitlines(), 1):
                s = line.strip()
                if not is_cmd(s):
                    continue
                if s.startswith(("if ", "for ", "while ", "case ")):
                    continue
                if not s.startswith(ALLOWED_PREFIXES):
                    warns.append((str(doc), i, f"line {ln}: uncommon prefix -> {s}"))

    print(f"[docs-check] scanned files: {len(DOCS)}")
    print(f"[docs-check] tested blocks: {tested}")
    if warns:
        print("[docs-check] warnings:")
        for d, i, w in warns:
            print(f"  - {d} block#{i}: {w}")
    if failures:
        print("[docs-check] failures:")
        for d, i, e in failures:
            print(f"  - {d} block#{i}: {e}")
        return 1
    print("[docs-check] OK")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

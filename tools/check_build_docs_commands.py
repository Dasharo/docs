#!/usr/bin/env python3
from __future__ import annotations
import argparse
import re
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DOCS = sorted((ROOT / "docs" / "variants").glob("**/building-manual.md"))
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

def should_skip_block(block: str) -> bool:
    b = block.lower()
    markers = ["<version>", "<variant>", "(docker)", "<path>"]
    return any(m in b for m in markers)

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

def pick_docs(files: list[str]) -> list[Path]:
    if not files:
        return DEFAULT_DOCS
    out = []
    for f in files:
        p = (ROOT / f).resolve() if not f.startswith('/') else Path(f)
        if p.exists() and p.name == 'building-manual.md' and str(p).startswith(str(ROOT)):
            out.append(p)
    return sorted(set(out))

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--files', nargs='*', default=[])
    args = ap.parse_args()

    docs = pick_docs(args.files)
    failures = []
    warns = []
    tested = 0

    if not docs:
        print("[docs-check] no target build-manual.md files selected")
        return 0

    for doc in docs:
        text = doc.read_text(encoding="utf-8", errors="ignore")
        for i, block in enumerate(extract_blocks(text), 1):
            tested += 1
            if should_skip_block(block):
                warns.append((str(doc), i, "placeholder/pseudocode block skipped"))
                continue
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

    print(f"[docs-check] scanned files: {len(docs)}")
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

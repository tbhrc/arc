#!/usr/bin/env python3
"""Package the canonical ARC Atlas Agent Skill as dist/skill.zip."""
from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".github" / "skills" / "atlas"
REQUIRED = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/modes.md",
)


def package_atlas(output: Path) -> Path:
    missing = [path for path in REQUIRED if not (SOURCE / path).is_file()]
    if missing:
        raise SystemExit("Missing Atlas package files: " + ", ".join(missing))

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(SOURCE.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts:
                continue
            relative = path.relative_to(SOURCE)
            archive.write(path, Path("atlas") / relative)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Package canonical ARC Atlas as skill.zip")
    parser.add_argument("--output", default=str(ROOT / "dist" / "skill.zip"))
    args = parser.parse_args()
    output = package_atlas(Path(args.output))
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

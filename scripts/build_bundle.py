# scripts/build_bundle.py
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = DOCS / "bundle.md"

# 結合したい順番（ここは雨宮さんの構成に合わせて増やしてOK）
FILES = [
    DOCS / "handbook.md",                 # 本編（例）
    DOCS / "appendix" / "fCWAR.md",        # 付録
    # DOCS / "appendix" / "wCWAR.md",
    # DOCS / "appendix" / "xCost.md",
]

header = """# Cooking Metrics Handbook (Bundle)

これはAIに投げる用の結合版です。正本はdocs配下の各ファイルです。

- 思想：継続と機嫌が最優先
- 正確さ：誤差OK
- 注意：勝手に新しい指標（Effort/Health等）を生やさないこと

---

"""

def normalize(md: str) -> str:
    # 末尾の空行を整えるくらい（過剰な加工はしない）
    return md.strip() + "\n"

parts = [header]
for f in FILES:
    if not f.exists():
        raise FileNotFoundError(f"Missing: {f}")
    title = f"\n\n---\n\n<!-- source: {f.relative_to(ROOT)} -->\n\n"
    parts.append(title)
    parts.append(normalize(f.read_text(encoding="utf-8")))

OUT.write_text("".join(parts), encoding="utf-8")
print(f"wrote: {OUT}")

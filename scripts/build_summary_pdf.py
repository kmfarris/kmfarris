"""Build docs/RESEARCH_AND_SYSTEMS_SUMMARY.pdf from the markdown (needs `markdown` and LibreOffice)."""

import pathlib
import re
import shutil
import subprocess
import tempfile

import markdown

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "docs" / "RESEARCH_AND_SYSTEMS_SUMMARY.md"
OUT = ROOT / "docs" / "RESEARCH_AND_SYSTEMS_SUMMARY.pdf"

CSS = """@page{size:letter;margin:0.45in}
body{font-family:'DejaVu Sans',sans-serif;font-size:8pt;line-height:1.2;margin:0}
h1{font-size:13pt;margin:0 0 1pt}h2{font-size:10pt;margin:5pt 0 1pt;border-bottom:1px solid #999}
p{margin:2pt 0 0}li{margin:0}ul{margin:0 0 0 12pt;padding:0}hr{display:none}code{font-size:7.5pt}a{color:#0645ad}"""


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    # Python-Markdown needs a blank line between a paragraph and the list that follows it.
    text = re.sub(r"(\*\*[^\n]*\*\*[^\n]*)\n- ", r"\1\n\n- ", text)
    body = markdown.markdown(text, extensions=["extra"])
    with tempfile.TemporaryDirectory() as tmp:
        html = pathlib.Path(tmp) / "summary.html"
        html.write_text(
            f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>",
            encoding="utf-8",
        )
        subprocess.run(
            ["libreoffice", "--headless", "--convert-to", "pdf:writer_web_pdf_Export", "--outdir", tmp, str(html)],
            check=True,
            capture_output=True,
        )
        shutil.copy(pathlib.Path(tmp) / "summary.pdf", OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

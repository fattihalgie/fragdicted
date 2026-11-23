"""Ubah file .py bertanda # %% jadi notebook .ipynb.
Pemakaian: python _to_ipynb.py sumber.py tujuan.ipynb
"""
import json
import sys

src, dst = sys.argv[1], sys.argv[2]
text = open(src, encoding="utf-8").read()

cells = []
for block in text.split("# %%"):
    block = block.strip("\n")
    if not block.strip():
        continue
    kind = "code"
    lines = block.splitlines()
    if lines[0].strip().startswith("[markdown]"):
        kind = "markdown"
        lines = lines[1:]
    body = "\n".join(lines).strip("\n")
    if not body.strip():
        continue
    cells.append({
        "cell_type": kind,
        "metadata": {},
        "source": body.splitlines(keepends=True),
        **({"execution_count": None, "outputs": []} if kind == "code" else {}),
    })

nb = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.14"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

with open(dst, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print(f"OK {dst} ({len(cells)} sel)")

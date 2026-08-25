#!/usr/bin/env python3
"""把 design-canvas (.dc) HTML 轉成可以直接用瀏覽器打開的單檔預覽。"""

import re, os, html, pathlib

SRC = pathlib.Path("./source")
REFACTORED = pathlib.Path("./source")
OUT = pathlib.Path("./preview")
RUNTIME = pathlib.Path("./tools/dc-runtime.js").read_text(encoding="utf-8")

FILES = {
    "Library_System_dc.html":  ("Library_System.html", "管理端 Admin Console"),
    "Patron_Portal_dc.html":   ("Patron_Portal.html",  "讀者端 Patron Portal"),
    "Wireframes_dc.html":      ("Wireframes.html",     "線框稿 Wireframes"),
}
LINK_FIX = {
    "Patron Portal.dc.html": "Patron_Portal.html",
    "Library System.dc.html": "Library_System.html",
}

NAV = """
<nav class="dc-preview-bar">
  <a href="./index.html">← 全部畫面</a>
  <span>{label}</span>
</nav>
<style>
  .dc-preview-bar{{position:fixed;right:16px;bottom:16px;z-index:2147483000;display:flex;align-items:center;gap:10px;
    background:rgba(28,28,28,.9);color:#fff;border-radius:999px;padding:7px 14px 7px 13px;
    font:500 12px/1 "Plus Jakarta Sans","Noto Sans TC",system-ui,sans-serif;
    box-shadow:0 8px 28px rgba(0,0,0,.28);backdrop-filter:blur(12px);
    opacity:.4;transition:opacity .18s ease-out;}}
  .dc-preview-bar:hover{{opacity:1}}
  .dc-preview-bar a{{color:#fff;text-decoration:none}}
  .dc-preview-bar a:hover{{color:#fff}}
  .dc-preview-bar span{{opacity:.55;border-left:1px solid rgba(255,255,255,.25);padding-left:10px}}
  @media print{{.dc-preview-bar{{display:none}}}}
</style>
<script>if (window.self !== window.top) document.querySelector(".dc-preview-bar").style.display = "none";</script>
"""


def split_source(text: str):
    """回傳 (helmet_head, template_markup, dc_script)。"""
    helmet = ""
    m = re.search(r"<helmet[^>]*>(.*?)</helmet>", text, re.S)
    if m:
        helmet = m.group(1).strip()
        text = text[:m.start()] + text[m.end():]

    script = ""
    m = re.search(r'<script[^>]*type="text/x-dc"[^>]*>(.*?)</script>', text, re.S)
    if m:
        script = m.group(1).strip()
        text = text[:m.start()] + text[m.end():]

    m = re.search(r"<x-dc[^>]*>(.*?)</x-dc>", text, re.S)
    body = m.group(1) if m else text
    return helmet, body.strip(), script


def clean_head(helmet: str) -> str:
    # 拿掉編輯器專用的 meta，保留字型與 style
    helmet = re.sub(r'<meta name="design_doc_mode"[^>]*/?>\s*', "", helmet)
    return helmet.strip()


def build(src_name: str, out_name: str, label: str):
    path = REFACTORED / src_name
    if not path.exists():
        path = SRC / src_name
    raw = path.read_text(encoding="utf-8")
    for old, new in LINK_FIX.items():
        raw = raw.replace(f'href="{old}"', f'href="{new}"')

    head, body, script = split_source(raw)
    head = clean_head(head)
    title = f"承光圖書館・{label}"
    nav = NAV.format(label=label)

    if script:  # 互動式畫面：樣板 + 執行環境
        page = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
{head}
</head>
<body>
<div id="dc-root"></div>

<template id="dc-tpl">
{body}
</template>

{nav}
<script>
{RUNTIME}
</script>
<script>
{script}

document.addEventListener("DOMContentLoaded", function () {{
  DC.mount(new Component(), document.getElementById("dc-root"), document.getElementById("dc-tpl"));
}});
</script>
</body>
</html>
"""
    else:  # 靜態畫面（線框稿）
        page = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
{head}
</head>
<body>
{body}
{nav}
</body>
</html>
"""

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / out_name).write_text(page, encoding="utf-8")
    print(f"✓ {out_name}  ({len(page):,} bytes)")


if __name__ == "__main__":
    for src, (out, label) in FILES.items():
        build(src, out, label)

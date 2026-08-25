#!/usr/bin/env python3
"""把兩個 design-canvas 原始檔對齊 Design_System_承光圖書館.md。

處理四件事：
  1. 字級收斂到規範的階梯（等寬資料另有一組）
  2. 圓角收斂到 4 / 12 / 16 / 20 / 24 / 99
  3. 淺色底上的紅字改用 #B7262A
  4. 補上過場、按下 scale(0.95)、鍵盤焦點樣式
"""

import re, pathlib, collections

SRC = pathlib.Path("./source")
DST = pathlib.Path("./source")
FILES = ["Library_System_dc.html", "Patron_Portal_dc.html"]

report = collections.Counter()

# ── 1. 字級：舊值 → 新值 ────────────────────────────────────────────
FONT_MAP = {
    "40": "40", "28": "28", "27": "28", "26": "28", "24": "24", "20": "20",
    "18": "20", "17": "15", "16.5": "15", "16": "15", "15": "15",
    "14.5": "15", "14": "13.5", "13.5": "13.5", "13": "13.5",
    "12.5": "12.5", "12": "12.5", "11.5": "11.5", "11": "11.5", "10.5": "10.5",
}
# 等寬（機器資料）自成一組：主要 12、次要 11.5
MONO_MAP = {"12": "12", "11.5": "11.5", "11": "11.5", "13.5": "12", "12.5": "12"}

# ── 2. 圓角 ────────────────────────────────────────────────────────
RADIUS_MAP = {"4": "4", "5": "4", "10": "12", "11": "12", "12": "12",
              "14": "16", "16": "16", "18": "20", "20": "20", "24": "24", "99": "99"}


def fix_style(style: str) -> str:
    is_mono = "Plex Mono" in style
    # 主要 CTA（實心紅按鈕）維持 14px 的 button-lg
    is_cta = "background: #DC2F33" in style and "font-weight: 600" in style

    def font(m):
        old = m.group(1)
        if is_mono:
            new = MONO_MAP.get(old, old)
        elif is_cta and old == "14":
            new = "14"
        else:
            new = FONT_MAP.get(old, old)
        if new != old:
            report[f"font-size {old} → {new}"] += 1
        return f"font-size: {new}px"

    style = re.sub(r"font-size:\s*([\d.]+)px", font, style)

    def radius(m):
        old, new = m.group(1), RADIUS_MAP.get(m.group(1), m.group(1))
        if new != old:
            report[f"border-radius {old} → {new}"] += 1
        return f"border-radius: {new}px"

    style = re.sub(r"border-radius:\s*([\d.]+)px", radius, style)

    # 淺色底上的紅字 → #B7262A
    if "color: #DC2F33" in style:
        style = style.replace("color: #DC2F33", "color: #B7262A")
        report["紅字 #DC2F33 → #B7262A"] += 1

    # 表格細線統一成 hairline
    if "1px solid #F2F3F4" in style:
        style = style.replace("1px solid #F2F3F4", "1px solid #E6E8EA")
        report["表格分隔線 #F2F3F4 → #E6E8EA"] += 1

    # 表頭 / 表格列內距收斂到 24
    for old, new in (("padding: 13px 22px", "padding: 12px 24px"),
                     ("padding: 14px 22px", "padding: 14px 24px")):
        if old in style:
            style = style.replace(old, new)
            report[f"{old} → {new}"] += 1

    return style


SYSTEM_CSS = """
  /* ── 設計規範：過場、按下、焦點 ───────────────────────────── */
  :root { --ease: cubic-bezier(0.25, 0.1, 0.25, 1); }
  [role="button"], input, a {
    transition: background-color 150ms var(--ease), color 150ms var(--ease),
                border-color 150ms var(--ease), opacity 150ms var(--ease),
                transform 150ms var(--ease);
  }
  /* pill 形狀＝動作，按下縮 5% */
  [role="button"][style*="border-radius: 99px"]:active { transform: scale(0.95); }
  [role="button"]:focus-visible,
  a:focus-visible { outline: 2px solid #DC2F33; outline-offset: 2px; }
  input:focus-visible { outline: 2px solid #DC2F33 !important; outline-offset: 2px; }
  @media (prefers-reduced-motion: reduce) {
    [role="button"], input, a { transition: none; }
    [role="button"][style*="border-radius: 99px"]:active { transform: none; }
  }
"""


def refactor(name: str):
    raw = (SRC / name).read_text(encoding="utf-8")
    head, rest = raw.split('<script type="text/x-dc"', 1)
    js = '<script type="text/x-dc"' + rest

    # 1–3：所有 style 屬性
    head = re.sub(r'style(-hover)?="([^"]*)"',
                  lambda m: f'style{m.group(1) or ""}="{fix_style(m.group(2))}"', head)

    # 連結色（在 #F7F8F9 上 4.39:1，不到 AA）
    if "a { color: #DC2F33;" in head:
        head = head.replace("a { color: #DC2F33;", "a { color: #B7262A;")
        head = head.replace("a:hover { color: #B7262A; }", "a:hover { color: #DC2F33; }")
        report["連結色 #DC2F33 → #B7262A"] += 1

    # 4：可點元素補上 role / tabindex
    def clickable(m):
        report["加上 role=button / tabindex"] += 1
        return m.group(0)[:-1] + ' role="button" tabindex="0">' if m.group(0).endswith(">") else m.group(0)

    head = re.sub(r'<div(?=[^>]*\sonClick=")((?:[^>"]|"[^"]*")*)>',
                  lambda m: (report.update(["加上 role=button / tabindex"]) or
                             f'<div{m.group(1)} role="button" tabindex="0">'), head)

    # 系統 CSS 併進 helmet 的 <style>
    head = head.replace("  ::placeholder { color: #9DA2A8; }",
                        "  ::placeholder { color: #9DA2A8; }\n" + SYSTEM_CSS, 1)

    # JS 裡的紅字（dueFg / actFg 之類）
    def js_fg(line):
        if re.search(r"\b\w*[Ff]g:", line) and "#DC2F33" in line:
            report["JS 內紅字 #DC2F33 → #B7262A"] += line.count("#DC2F33")
            return line.replace("#DC2F33", "#B7262A")
        return line

    js = "\n".join(js_fg(l) for l in js.split("\n"))
    js = js.replace('border-bottom: 1px solid #F2F3F4', 'border-bottom: 1px solid #E6E8EA')

    DST.mkdir(parents=True, exist_ok=True)
    (DST / name).write_text(head + js, encoding="utf-8")
    print(f"✓ {name}")


if __name__ == "__main__":
    for f in FILES:
        refactor(f)
    print("\n變更統計")
    for k, v in sorted(report.items(), key=lambda kv: -kv[1]):
        print(f"  {v:>4}×  {k}")

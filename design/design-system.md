---
version: 1.0
name: chengguang-library-design-system
description: 承光圖書館的設計語言。骨架取自 Apple 的網頁規範——單一動作色、以表面換色代替裝飾、只有一種陰影、卡片一律用細線而非陰影、按下時 scale(0.95)——但把 Apple 的 Action Blue 換成專案原本的承光紅 #DC2F33，並把行銷網頁的低密度調整成圖書館後台需要的資料密度。白底卡片浮在 #F7F8F9 畫布上，深色只出現在登入 tile 與 modal 遮罩，紅色只出現在「可以按」和「要注意」兩件事上。

colors:
  primary: "#DC2F33"
  primary-press: "#B7262A"
  primary-on-dark: "#FF6B63"
  primary-tint: "#FDF0F0"
  primary-tint-strong: "#FDE3E3"
  primary-tint-border: "#F3CACB"
  ink: "#1C1C1C"
  ink-80: "#3A3E43"
  ink-64: "#5C6166"
  ink-56: "#6B7075"
  ink-40: "#8B9096"
  ink-32: "#9DA2A8"
  ink-24: "#AEB3B8"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  on-dark-muted: "#E4E6E9"
  on-dark-subtle: "#B0B4B8"
  canvas: "#F7F8F9"
  surface: "#FFFFFF"
  surface-input: "#FAFBFC"
  surface-chip: "#F2F3F4"
  surface-chip-alt: "#EFF0F2"
  surface-tile-dark: "#1C1C1C"
  surface-black: "#000000"
  hairline: "#E6E8EA"
  hairline-strong: "#DDE0E3"
  scrim: "rgba(0, 0, 0, 0.5)"

typography:
  hero-display:
    fontFamily: "Plus Jakarta Sans, Noto Sans TC, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -1.4px
  display-lg:
    fontFamily: "Plus Jakarta Sans, Noto Sans TC, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.8px
  display-md:
    fontFamily: "Plus Jakarta Sans, Noto Sans TC, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.6px
  section-title:
    fontFamily: "Plus Jakarta Sans, Noto Sans TC, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: -0.4px
  card-title:
    fontFamily: "Plus Jakarta Sans, Noto Sans TC, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: -0.2px
  lede:
    fontFamily: "Plus Jakarta Sans, Noto Sans TC, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: 0
  body:
    fontFamily: "Plus Jakarta Sans, Noto Sans TC, system-ui, sans-serif"
    fontSize: 13.5px
    fontWeight: 500
    lineHeight: 1.75
    letterSpacing: 0
  body-strong:
    fontFamily: "Plus Jakarta Sans, Noto Sans TC, system-ui, sans-serif"
    fontSize: 13.5px
    fontWeight: 700
    lineHeight: 1.75
    letterSpacing: 0
  label:
    fontFamily: "Plus Jakarta Sans, Noto Sans TC, system-ui, sans-serif"
    fontSize: 12.5px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "Plus Jakarta Sans, Noto Sans TC, system-ui, sans-serif"
    fontSize: 12.5px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  micro:
    fontFamily: "Plus Jakarta Sans, Noto Sans TC, system-ui, sans-serif"
    fontSize: 11.5px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  eyebrow:
    fontFamily: "Plus Jakarta Sans, Noto Sans TC, system-ui, sans-serif"
    fontSize: 10.5px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0.6px
    textTransform: uppercase
  data:
    fontFamily: "IBM Plex Mono, ui-monospace, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  data-strong:
    fontFamily: "IBM Plex Mono, ui-monospace, monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  data-sm:
    fontFamily: "IBM Plex Mono, ui-monospace, monospace"
    fontSize: 11.5px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button:
    fontFamily: "Plus Jakarta Sans, Noto Sans TC, system-ui, sans-serif"
    fontSize: 13.5px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0
  button-lg:
    fontFamily: "Plus Jakarta Sans, Noto Sans TC, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 12px
  md: 16px
  lg: 20px
  xl: 24px
  pill: 99px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 20px
  xl: 24px
  xxl: 32px
  section: 40px
  page: 56px

motion:
  press: "transform: scale(0.95)"
  duration: 150ms
  easing: "cubic-bezier(0.25, 0.1, 0.25, 1)"

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 13px 22px
  button-primary-press:
    backgroundColor: "{colors.primary-press}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-80}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 13px 22px
  button-ghost-danger:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-press}"
    border: "1px solid {colors.primary-tint-border}"
    typography: "{typography.micro}"
    rounded: "{rounded.pill}"
    padding: 7px 14px
  button-dark:
    backgroundColor: "{colors.surface-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 20px
  filter-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-80}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 18px
  filter-pill-selected:
    backgroundColor: "{colors.surface-black}"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.surface-black}"
    rounded: "{rounded.pill}"
  input:
    backgroundColor: "{colors.surface-input}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 14px
  search-input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 11px 18px
    height: 44px
  sidebar:
    backgroundColor: "{colors.surface}"
    borderRight: "1px solid {colors.hairline}"
    width: 248px
    padding: 26px 18px
  nav-item:
    backgroundColor: transparent
    textColor: "{colors.ink-80}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 11px 13px
  nav-item-selected:
    backgroundColor: "{colors.primary-tint}"
    textColor: "{colors.primary-press}"
    rounded: "{rounded.sm}"
  topbar-frosted:
    backgroundColor: "rgba(247, 248, 249, 0.92)"
    backdropFilter: "blur(8px)"
    borderBottom: "1px solid {colors.hairline}"
    height: 61px
    padding: 18px 34px
  card:
    backgroundColor: "{colors.surface}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  card-alert:
    backgroundColor: "{colors.primary-tint}"
    border: "1px solid {colors.primary-tint-border}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  panel-inset:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: 15px 16px
  table-header:
    backgroundColor: "{colors.surface-input}"
    textColor: "{colors.ink-56}"
    typography: "{typography.micro}"
    fontWeight: 600
    borderBottom: "1px solid {colors.hairline}"
    padding: 12px 24px
  table-row:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    borderBottom: "1px solid {colors.hairline}"
    padding: 14px 24px
  status-chip-neutral:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-80}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.micro}"
    rounded: "{rounded.pill}"
    padding: 5px 11px
  status-chip-alert:
    backgroundColor: "{colors.primary-tint-strong}"
    textColor: "{colors.primary-press}"
    typography: "{typography.micro}"
    rounded: "{rounded.pill}"
    padding: 5px 11px
  status-chip-done:
    backgroundColor: "{colors.surface-chip-alt}"
    textColor: "{colors.ink-64}"
    typography: "{typography.micro}"
    rounded: "{rounded.pill}"
    padding: 5px 11px
  quota-meter:
    trackColor: "{colors.surface-chip}"
    fillColor: "{colors.ink}"
    fillColorFull: "{colors.primary}"
    rounded: "{rounded.pill}"
    height: 6px
  modal:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.xl}"
    padding: 30px 32px
    maxWidth: 620px
    scrim: "{colors.scrim}"
  toast:
    backgroundColor: "{colors.surface-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 13px 22px
    shadow: "0 8px 28px rgba(0, 0, 0, 0.28)"
  auth-tile-dark:
    backgroundColor: "{colors.surface-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.hero-display}"
    rounded: "{rounded.none}"
    padding: 56px 48px
  auth-card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.xl}"
    padding: 36px
    maxWidth: 400px
---

## 總覽 Overview

這套語言的骨架是 Apple 的：**介面自己退到後面，讓內容說話**。差別在於 Apple 的內容是產品照片，你的內容是資料——書名、ISBN、應還日、還剩幾天。所以規則的形狀一樣，數值不一樣：Apple 用 80px 的區塊留白，你用 20px 的卡片內距；Apple 的正文是 17px，你的正文是 13.5px。**照抄 Apple 的密度會讓後台變得難用**，照抄它的紀律則會讓後台變得好看。

三個共通的紀律，這份規範會反覆回到它們：

1. **只有一個動作色。** Apple 全站只有 Action Blue，你全站只有承光紅 `{colors.primary}`。紅色出現的地方只有兩種：可以按的東西、需要注意的東西（逾期、借滿、刪除）。其他一律是墨色與灰階。
2. **層次靠換表面，不靠陰影。** 白卡片浮在 `{colors.canvas}` 畫布上，靠 1px 的 `{colors.hairline}` 分界。整套系統只有一種陰影，而且只給真正浮在內容之上的東西（toast）。
3. **形狀有文法。** 圓角不是隨手選的：`{rounded.pill}` 代表「這是動作或狀態」，`{rounded.sm}` 代表「這是可輸入的欄位或列」，`{rounded.lg}` / `{rounded.xl}` 代表「這是一塊容器」。中間值不存在。

**這套系統的識別特徵：**

- 承光紅 `{colors.primary}` 是唯一的品牌互動色；深色底上換成 `{colors.primary-on-dark}`，淡紅底上換成 `{colors.primary-press}`（見〈顏色〉的對比度說明）。
- 畫布是 `{colors.canvas}`、卡片是純白——這是 Apple 的反轉版本，也是後台介面應該有的樣子（Apple 網頁的預設畫布是白，off-white 用來換節奏；資料介面必須反過來，卡片才有邊界）。
- 純黑 `{colors.surface-black}` 只出現在三個地方：登入頁的品牌 tile、選取中的篩選 pill、toast。它是「終點」的顏色，不是背景色。
- 中文主標 ＋ 英文副標的雙語配對（「借閱管理 Loans」）是這套介面最好認的簽名，有一組專屬規則，見〈雙語排版〉。
- 機器資料（ISBN、證號、日期、金額）一律走 `{typography.data}` 的 IBM Plex Mono，人讀的文字一律走 Plus Jakarta Sans ＋ Noto Sans TC。這條界線不能模糊。
- 唯一的陰影：`0 8px 28px rgba(0, 0, 0, 0.28)`，只給 toast。卡片、按鈕、輸入框永遠沒有陰影。
- 表頭固定、側欄固定，`backdrop-filter: blur(8px)` 的半透明頂欄——這點你原本的設計和 Apple 的 frosted sub-nav 是同一個做法。

## Apple 規範 → 承光的對照

| Apple 的規則 | 承光怎麼做 | 為什麼 |
|---|---|---|
| 單一 Action Blue `#0066cc` | 單一承光紅 `{colors.primary}` | 同一條紀律，換色相 |
| 深色底改用 Sky Link Blue `#2997ff` | 深色底改用 `{colors.primary-on-dark}` | 紅色在 `{colors.ink}` 上只有 3.65:1，一定要調亮 |
| 畫布白、parchment 換節奏 | 畫布 `{colors.canvas}`、卡片白 | 資料卡片需要邊界，反轉才成立 |
| 正文 17px / 行高 1.47 | 正文 13.5px / 行高 1.75 | 後台密度；中文字需要更多行距 |
| 字重階梯 300 / 400 / 600 / 700，刻意沒有 500 | 400 / 500 / 600 / 700 / 800，500 是 UI 預設 | Plus Jakarta Sans 的 400 在小字級偏細，中文更明顯 |
| 圓角 8 / 11 / 18 / pill | 12 / 16 / 20 / 24 / pill | 你的設計語彙比 Apple 更圓，維持它，但收斂成 4 的倍數 |
| 整站一種陰影，只給產品照 | 整站一種陰影，只給 toast | 同一條紀律；你沒有產品照，浮層就是那個例外 |
| 全出血 tile 交替明暗當分隔 | 卡片 ＋ 1px 細線分隔 | 後台沒有全出血區塊，細線是它的等價物 |
| 按下 `scale(0.95)` | 按下 `scale(0.95)`，150ms | 直接沿用 |
| 不記錄 hover，只有預設與按下 | 記錄 hover（`{colors.primary-press}`、`{colors.surface-chip}`） | 桌機後台以滑鼠為主，hover 是必要的回饋 |

## 顏色 Colors

### 動作色

- **承光紅**（`{colors.primary}` — #DC2F33）：唯一的品牌互動色。主要按鈕底、選取指示點、進度條滿載狀態、危險操作的文字。白字放在它上面是 4.67:1，通過 AA。
- **按下／淺底紅字**（`{colors.primary-press}` — #B7262A）：兩個用途——按鈕按下與 hover 的底色；以及**任何放在淺色底上的紅色文字**。這條規則有數字支撐：`{colors.primary}` 當文字放在 `{colors.canvas}` 上只有 4.39:1、放在 `{colors.primary-tint}` 上只有 4.20:1，都低於 AA 的 4.5；換成 `{colors.primary-press}` 分別是 5.94 與 5.69，安全。純白底上的 `{colors.primary}` 其實是 4.67，剛好過關，但**規則不留例外**：紅色當文字就是 #B7262A，當底色才是 #DC2F33。
- **深底上的紅**（`{colors.primary-on-dark}` — #FF6B63）：放在 `{colors.ink}` 或 `{colors.surface-black}` 上的紅色連結與強調（6.12:1 / 7.54:1）。**不要在淺色底上用它**，就像 Apple 不在白底用 Sky Link Blue。
- **紅色淡底**（`{colors.primary-tint}` — #FDF0F0）：選取中的側欄項、提示條、可借出的選取列。
- **警示淡底**（`{colors.primary-tint-strong}` — #FDE3E3）：逾期 chip、逾期計數的底。比 tint 再深一階，代表「這件事需要處理」而不只是「這件事被選到」。
- **淡底邊框**（`{colors.primary-tint-border}` — #F3CACB）：淡紅底上的 1px 邊，也用在 ghost danger 按鈕。

### 表面

- **畫布**（`{colors.canvas}` — #F7F8F9）：所有頁面的底色，也是卡片內嵌面板的底。
- **卡片**（`{colors.surface}` — #FFFFFF）：卡片、表格、側欄、modal、頂欄。
- **輸入框**（`{colors.surface-input}` — #FAFBFC）：只給輸入框。比畫布再淺一階，讓欄位在白卡片上仍然讀得出是可填的區域。
- **中性 chip**（`{colors.surface-chip}` — #F2F3F4 / `{colors.surface-chip-alt}` — #EFF0F2）：分段控制的軌道、進度條軌道、已完成狀態的 chip 底。
- **深 tile**（`{colors.surface-tile-dark}` — #1C1C1C）與**純黑**（`{colors.surface-black}` — #000000）：登入頁的品牌側、選取中的 pill、toast。純黑是刻意的，登入頁的紅色方塊 logo 在純黑上最亮。
- **遮罩**（`{colors.scrim}` — rgba(0,0,0,0.5)）：modal 背後。

### 文字

一條墨色階梯，數字代表「大約多濃」，不是不透明度：

| Token | 色值 | 白底對比 | 用在哪 |
|---|---|---|---|
| `{colors.ink}` | #1C1C1C | 17.0:1 | 標題、表格主要欄位、數值 |
| `{colors.ink-80}` | #3A3E43 | 10.8:1 | 未選取的側欄項、次要按鈕文字 |
| `{colors.ink-64}` | #5C6166 | 6.3:1 | 欄位標籤、說明文字 |
| `{colors.ink-56}` | #6B7075 | 5.0:1 | 副標、卡片說明——**小字級的安全下限** |
| `{colors.ink-40}` | #8B9096 | 3.2:1 | 表頭、輔助標記（不可用於正文） |
| `{colors.ink-32}` | #9DA2A8 | 2.6:1 | placeholder、英文副標 |
| `{colors.ink-24}` | #AEB3B8 | 2.1:1 | 停用狀態、分隔符號 |

`{colors.ink-40}` 以下都低於 AA，只能用在「看不到也不影響操作」的資訊上（表頭、placeholder、裝飾性副標）。**任何使用者需要讀懂才能完成任務的文字，最淡只能到 `{colors.ink-56}`。**

深色底上：主要文字 `{colors.on-dark}`、次要 `{colors.on-dark-muted}`（#E4E6E9）、再次要 `{colors.on-dark-subtle}`（#B0B4B8）。

### 細線

- `{colors.hairline}`（#E6E8EA）：預設的 1px 邊框與分隔線。卡片、表格列、輸入框、側欄右界都用它。
- `{colors.hairline-strong}`（#DDE0E3）：需要再明確一點的分隔（表格內的欄位切分、停用邊框）。

### 漸層

**沒有漸層。** 和 Apple 一樣，這套系統裡沒有任何裝飾性漸層。深淺的變化一律由表面換色產生。唯一的例外是進度條的填色，那是資料，不是裝飾。

## 字體 Typography

### 字族

- **介面／標題**：`Plus Jakarta Sans` — 幾何感、字腔開，數字辨識度高，在 13.5px 仍然清楚。
- **中文**：`Noto Sans TC` — 和 Plus Jakarta Sans 的字重階梯對得上（400/500/700）。永遠寫在英文字族後面，讓拉丁字母走 Jakarta、漢字走 Noto。
- **資料**：`IBM Plex Mono` — ISBN、使用者證號、日期、金額。等寬讓縱向掃描時數字對齊，這是後台最重要的閱讀動作。

### 階梯

| Token | 級數 | 字重 | 行高 | 字距 | 用在哪 |
|---|---|---|---|---|---|
| `{typography.hero-display}` | 40px | 800 | 1.15 | -1.4px | 登入頁主標，全站只有這裡 |
| `{typography.display-lg}` | 28px | 700 | 1.25 | -0.8px | 頁面主標題（借閱管理、我的借閱） |
| `{typography.display-md}` | 24px | 700 | 1.3 | -0.6px | modal 標題、登入卡標題 |
| `{typography.section-title}` | 20px | 700 | 1.35 | -0.4px | 區塊標題、KPI 數值 |
| `{typography.card-title}` | 15px | 700 | 1.4 | -0.2px | 卡片標題、書名 |
| `{typography.lede}` | 15px | 400 | 1.8 | 0 | 登入頁的說明段落、區塊開頭的長句 |
| `{typography.body}` | 13.5px | 500 | 1.75 | 0 | 正文、表格內容、按鈕以外的一切 |
| `{typography.body-strong}` | 13.5px | 700 | 1.75 | 0 | 表格中需要被先看到的欄位（姓名、書名） |
| `{typography.label}` | 12.5px | 600 | 1.4 | 0 | 表單欄位標籤 |
| `{typography.caption}` | 12.5px | 400 | 1.7 | 0 | 說明文字、卡片副標 |
| `{typography.micro}` | 11.5px | 400 | 1.6 | 0 | 狀態 chip、英文副標、附註 |
| `{typography.eyebrow}` | 10.5px | 600 | 1.0 | 0.6px | 全大寫的分區標（ADMIN CONSOLE、CATEGORY） |
| `{typography.data}` | 12px | 400 | 1.4 | 0 | 主要的機器字串：ISBN 欄、日期、金額 |
| `{typography.data-sm}` | 11.5px | 400 | 1.4 | 0 | 附在人名或書名下的次要機器字串（證號、ISBN 副行） |
| `{typography.button}` | 13.5px | 600 | 1.0 | 0 | 按鈕、篩選 pill |

### 原則

- **顯示級距一律負字距。** 40px 用 -1.4px、28px 用 -0.8px、20px 用 -0.4px，大致是 -0.035em 的比例。這是 Apple 標題手感的來源，Plus Jakarta Sans 的預設字距偏寬，不收緊會鬆散。**13.5px 以下不要用負字距**，中文會黏在一起。
- **中文需要比 Apple 更大的行距。** Apple 正文用 1.47，這套用 1.75。漢字沒有 x-height 的視覺休息點，行距不夠就變成一堵牆。段落型的說明文字可以到 1.8。
- **字重階梯是 400 / 500 / 600 / 700 / 800。** 500 是 UI 的預設（不是 400），因為 Plus Jakarta Sans 的 400 在 13.5px 偏細，配 Noto Sans TC 的 400 更明顯。800 只給登入頁主標。
- **等寬字只給機器產生的字串。** ISBN、`U-2019-0384`、`2026-09-01`、`NT$1,680` 走 `{typography.data}`；書名、姓名、分類、出版商是人讀的，走一般字族。**不要用等寬字排中文。**
- **級數階梯不要再擴充。** 現有介面同時出現 11 / 11.5 / 12 / 12.5 / 13 / 13.5 / 14，肉眼分不出來但會讓實作失去依據。收斂規則見〈落差檢查〉。

## 版面 Layout

### 間距

- **基準 4px。** 結構性間距用 8 / 12 / 16 / 20 / 24 / 32 / 40；6px 與 14px 保留給文字之間的微調（標題與副標、圖示與標籤）。
- **卡片內距** `{spacing.lg}`（20px），大卡片與 modal 用 24–32px。
- **卡片之間** 16–20px；區塊之間 `{spacing.section}`（40px）。
- **表格列內距** 14px × 24px；表頭 12px × 24px。（現況是 14px × 22px / 13px × 22px，收斂到 24 即可。）
- **按鈕內距**：主要 13px × 22px、次要 10px × 18px、小型 7px × 14px。

### 格線與容器

- **內容最大寬度 1240px**（管理端）／ **1180px**（讀者端），兩側 34px。
- **側欄固定 248px**，`position: sticky` 貼滿視窗高度。
- **卡片格線** `repeat(auto-fill, minmax(320px, 1fr))`，間距 16–18px。
- **表格用 CSS Grid 而不是 `<table>`**，欄寬用 fr 比例定義，數值欄固定 px（例如 `96px minmax(140px, 1.6fr) 130px 76px 128px`）。這樣表頭與列可以共用同一組欄位定義。

### 留白哲學

Apple 的留白是產品的台座；這裡的留白是**掃描的節拍**。使用者的動作是「一列一列往下看，找出逾期的那筆」，所以留白要規律而不是壯闊：每列高度一致、每個 chip 的內距一致、每張卡片的內距一致。**寧可整體再緊一點，也不要讓某一列比別列高。** 唯一該慷慨留白的地方是登入頁——那裡沒有資料要掃描，可以用 56px 以上的內距。

## 層次與深度 Elevation

| 層級 | 做法 | 用在哪 |
|---|---|---|
| 平面 | 無邊框、無陰影 | 頁面畫布、區塊 |
| 細線 | 1px `{colors.hairline}` | 卡片、表格、輸入框、側欄——**預設層級** |
| 換底色 | `{colors.canvas}` 或 `{colors.primary-tint}` | 內嵌面板、選取中的項目 |
| 毛玻璃 | `rgba(247,248,249,0.92)` ＋ `backdrop-filter: blur(8px)` | 固定頂欄 |
| 遮罩 | `{colors.scrim}` | modal 背後 |
| 陰影 | `0 8px 28px rgba(0,0,0,0.28)` | **只有 toast** |

**陰影哲學。** 整套系統只有一種陰影，而且只給真正浮在所有內容之上、會自己消失的東西。卡片不要陰影、按鈕不要陰影、modal 不要陰影（它用遮罩製造層次）。要強調某個東西時，順序是：換底色 → 加細線 → 換文字濃度 → 才輪到考慮位置。加陰影不在選項裡。

## 形狀 Shapes

| Token | 值 | 用在哪 |
|---|---|---|
| `{rounded.xs}` | 4px | logo 內的小方塊、進度條端點 |
| `{rounded.sm}` | 12px | 輸入框、側欄項、表單控制項 |
| `{rounded.md}` | 16px | 卡片內的內嵌面板、小卡 |
| `{rounded.lg}` | 20px | 主要卡片、表格容器 |
| `{rounded.xl}` | 24px | 登入卡、modal |
| `{rounded.pill}` | 99px | 按鈕、篩選 pill、狀態 chip、搜尋框、進度條 |

**圓角的文法：** pill 代表「這是動作或狀態」；12px 代表「這是可以輸入或點選的一列」；20 / 24px 代表「這是一塊容器」。容器越大圓角越大。**不要出現 8px、10px、14px、18px 這些中間值**——它們讓系統看起來像是每次都重新決定一次。

## 元件 Components

### 導覽

**`sidebar`** — 白底、右側 1px `{colors.hairline}`、寬 248px、`position: sticky`。由上到下：品牌區（34px 紅色圓角方塊 ＋ 中文名 ＋ `{typography.eyebrow}` 的英文分區）、導覽項、館規面板、底部的使用者與登出。

**`nav-item`** — 內距 11px × 13px、`{rounded.sm}`。左側 7px 的紅點只在選取時顯示（`opacity: 0` → `1`），選取時底色換成 `{colors.primary-tint}`、文字換成 `{colors.primary-press}`、字重 500 → 700。**紅點是這裡唯一的紅色物件，不要再加左側色條。** 需要提示數量時，右側放一顆 `{components.status-chip-alert}` 樣式的計數。

**`topbar-frosted`** — 半透明 ＋ `blur(8px)` 的固定頂欄，1px 下邊界。左側是全域搜尋（`{components.search-input}`），右側是跨端連結與今天的日期。日期用 `{typography.data}`。

### 按鈕

**`button-primary`** — `{colors.primary}` 底、白字、`{rounded.pill}`、13px × 22px。hover 換 `{colors.primary-press}`，按下 `scale(0.95)`。一個畫面同時最多**一顆**主要按鈕。

**`button-secondary`** — 白底、`{colors.hairline}` 邊、`{colors.ink-80}` 字、同樣 pill。用於「取消」以及和主要按鈕成對出現的次要動作。

**`button-ghost-danger`** — 白底、`{colors.primary-tint-border}` 邊、`{colors.primary}` 字、`{typography.micro}`、7px × 14px。用於表格列內的破壞性或不可逆動作（刪除、辦理歸還）。**列內動作永遠是 ghost，不能是實心紅**——一列一顆實心紅按鈕會讓整張表看起來都在警告。

**`filter-pill` / `filter-pill-selected`** — 未選：白底、細線邊、`{colors.ink-80}`。選取：`{colors.surface-black}` 底、白字。**篩選的選取態用黑色不用紅色**，因為紅色要留給「逾期」這種語意；篩選只是視角切換，不是警示。

### 卡片與容器

**`card`** — 白底、1px `{colors.hairline}`、`{rounded.lg}`、內距 20px。所有 KPI 卡、書卡、面板的基底。

**`card-alert`** — 同上但底色 `{colors.primary-tint}`、邊框 `{colors.primary-tint-border}`。只用在需要動作的統計（逾期筆數）。一個畫面最多一張。

**`table-header` / `table-row`** — Grid 排版。表頭 `{typography.micro}` ＋ `{colors.ink-40}`；列以 1px `{colors.hairline}` 分隔，最後一列不畫線。主要欄位（姓名、書名）用 `{typography.body-strong}`，其下的次要資訊（證號、ISBN）用 `{typography.data}` ＋ `{colors.ink-32}`。**逾期的應還日改成 `{colors.primary}` ＋ 字重 700**，這是表格裡唯一允許出現的紅色文字。

**`status-chip`** — 三個變體，語意固定：借閱中＝`{components.status-chip-neutral}`（白底細線）、逾期＝`{components.status-chip-alert}`（`{colors.primary-tint-strong}` 底 ＋ `{colors.primary-press}` 字）、已歸還＝`{components.status-chip-done}`（灰底灰字）。**chip 只放狀態，不放動作。**

**`quota-meter`** — 5 格的額度指示（借滿 5 本的規則直接視覺化）。已用的格子填 `{colors.ink}`、未用的填 `{colors.surface-chip}`；**借滿時整條換成 `{colors.primary}`**。這是紅色作為「狀態」而非「動作」的標準用法。

**`modal`** — `{colors.scrim}` 遮罩 ＋ 白卡 ＋ `{rounded.xl}` ＋ 內距 30–32px、最寬 620px。結構固定：標題 ＋ 一行說明 → 內容 → 右下角「取消（次要）／ 確認（主要）」。右上角一顆關閉。**確認鍵不可用時直接停用並在上方顯示原因**（例如「此使用者已借滿 5 本」），不要讓人按了才報錯。

**`toast`** — 黑底白字 pill，底部置中 30px，2.6 秒後消失，帶系統唯一的那顆陰影。文案用完成式並回應剛才的動作（「已歸還《小王子》」）。

### 表單

**`input`** — `{colors.surface-input}` 底、1px `{colors.hairline}`、`{rounded.sm}`、內距 12px × 14px。上方是 `{typography.label}` ＋ `{colors.ink-64}` 的標籤，標籤與欄位間距 6px。placeholder 用 `{colors.ink-32}`，而且**要放真實範例**（`978-986-xxx-xxx-x`、`2024-05-01`）而不是重複標籤文字。

**錯誤狀態** — 訊息放在欄位群組下方：`{colors.primary-tint}` 底、`{rounded.sm}`、`{colors.primary-press}` 字、12.5px。**不要只把邊框變紅**，光靠顏色傳達錯誤對色覺障礙使用者無效，一定要有文字。

## 雙語排版 Bilingual pairing

這是這套介面最好認的特徵，值得寫成規則：

- **主語言是中文，英文是註腳。** 順序永遠是「中文 英文」，中間一個半形空格，不加括號、不加斜線。
- **英文永遠比中文小一階、淡一階。** 導覽項「借閱管理 Loans」＝ 13.5px `{colors.ink-80}` ＋ 11.5px `{colors.ink-32}`；頁面標題「我的借閱 My loans」＝ 28px `{colors.ink}` ＋ 較小字級的 `{colors.ink-40}`。
- **全大寫的英文分區標**（ADMIN CONSOLE、CATEGORY、PUBLISHER）走 `{typography.eyebrow}`，字距 0.6px。這是唯一可以全大寫的地方。
- **不是每個字串都要配英文。** 導覽、頁面標題、欄位標籤、主要按鈕要配；表格內容、說明文字、toast 不配。過度配對會讓介面看起來像是翻譯練習。
- **中英混排時，數字與拉丁字母前後不加空格**（`借期 14 天`、`共 11 筆紀錄`），因為 Plus Jakarta Sans 與 Noto Sans TC 的側邊空間已經處理好了。

## Do / Don't

### Do

- 讓 `{colors.primary}` 是畫面上唯一的彩色。一個畫面裡紅色物件超過三個，就要重新想哪一個才是真正的動作。
- 淺色底上的紅色文字一律用 `{colors.primary-press}`（沒有例外，即使在白底上 `{colors.primary}` 剛好過關），深色底上一律用 `{colors.primary-on-dark}`。`{colors.primary}` 只當底色、邊框與指示點。
- 卡片一律 `{colors.hairline}` 1px 邊，沒有陰影。
- 顯示級距（20px 以上）加負字距；13.5px 以下不加。
- 表格列高與 chip 內距全站一致，掃描的節拍比任何裝飾都重要。
- 機器字串走 `{typography.data}`，人讀的字走一般字族。
- 按下用 `scale(0.95)`，過場 150ms。
- 停用狀態要說明原因（借滿、無庫存），不要只是變灰。

### Don't

- 不要引入第二個強調色。狀態的差異用 `{colors.primary-tint}` / `{colors.primary-tint-strong}` / `{colors.surface-chip-alt}` 的深淺去分，不要用綠色或橘色。
- 不要在 `{colors.primary-tint}` 或 `{colors.canvas}` 上直接用 `{colors.primary}` 當文字色（4.2:1 / 4.39:1，不到 AA）。
- 不要給卡片或按鈕加陰影。
- 不要用漸層當背景。
- 不要在表格列裡放實心紅按鈕。
- 不要把 `{colors.ink-40}` 以下的灰用在使用者必須讀懂的文字上。
- 不要混用圓角文法（pill 只給動作與狀態，容器不用 pill，欄位不用 20px）。
- 不要用等寬字排中文。
- 不要新增字級。要新的階層時，先改字重或濃度。

## 響應式 Responsive

| 名稱 | 寬度 | 主要變化 |
|---|---|---|
| 手機 | ≤ 640px | 側欄收成頂部橫向 tab；表格改為卡片式，每列變成一張卡；KPI 一欄；登入頁的深色 tile 收成頂部橫幅 |
| 平板直式 | 641–900px | 側欄收成 68px 的圖示欄（只留紅點與圖示）；卡片格線 2 欄；表格隱藏次要欄位（出版商、定價） |
| 平板橫式 | 901–1180px | 側欄回到 248px；卡片格線 2–3 欄；表格保留全部欄位但欄寬壓縮 |
| 桌機 | 1181–1440px | 完整版面；內容鎖在 1240px（管理端）／1180px（讀者端） |
| 寬螢幕 | ≥ 1441px | 內容維持鎖定寬度，多餘空間留給邊距，不要把表格拉寬 |

**點擊區至少 44 × 44px。** 目前列內的 ghost 按鈕（7px × 14px 內距）在觸控裝置上偏小，行動版要加大到 10px × 16px 或改成整列可點。

**收合策略：** 表格在窄螢幕不要橫向捲動，改成卡片；篩選 pill 列可以橫向捲動但要保留左右的漸隱提示；modal 在手機改為由下往上的全寬面板，圓角只留上方 `{rounded.xl}`。

## 落差檢查 Gap list

### 已套用到 `source/` 的原始檔

1. **字級收斂。** 原本同時存在 10.5 / 11 / 11.5 / 12 / 12.5 / 13 / 13.5 / 14 / 14.5 / 15 / 16 / 16.5 / 17 / 18 / 20 / 24 / 26 / 27 / 28 / 40 共二十種；現在只剩規範上的那幾階（一般字族 10.5 / 11.5 / 12.5 / 13.5 / 15 / 20 / 24 / 28 / 40，等寬 11.5 / 12）。實心紅的主要 CTA 保留 14px 的 `{typography.button-lg}`。
2. **淺色底上的紅字。** `a { color }`、逾期計數、逾期應還日、列內的刪除／辦理歸還按鈕全部改成 `{colors.primary-press}`。`{colors.primary}` 現在只出現在底色、邊框與指示點上——**紅色當文字時一律是 #B7262A**，這條規則沒有例外比較好記。
3. **圓角收斂。** 10 / 11 / 14 / 18 → 12 / 12 / 16 / 20。
4. **表格細線。** 列的下邊界原本是 `#F2F3F4`（那是 chip 的底色），改成 `{colors.hairline}`；表頭與列內距 22 → 24。
5. **過場。** 所有可點元素與輸入框加上 150ms 的 `background-color / color / border-color / transform` 過場，並包在 `prefers-reduced-motion` 的保護裡。
6. **按下狀態。** pill 形狀的可點元素按下時 `scale(0.95)`——用 `[role="button"][style*="border-radius: 99px"]:active` 選取，剛好對應「pill＝動作」的圓角文法。
7. **鍵盤焦點。** 可點的 `<div>` 補上 `role="button"` 與 `tabindex="0"`（共 42 個），並加上 `:focus-visible` 的 2px `{colors.primary}` 外框；輸入框的 `outline: none` 用 `!important` 覆蓋回來。

### 還沒做

8. **語意標籤。** `role="button"` ＋ `tabindex` 是可行的過渡做法，但真正實作時應該換成 `<button type="button">`，導覽區包 `<nav>`，表格用 `<table>` 或加上 `role="table"` 一類的標記。這一步會動到版面（button 的預設寬度是 fit-content，全寬的 CTA 需要補 `width: 100%`），所以留給實作階段。
9. **其餘間距收斂。** 11 / 13 / 26 / 30 之類的值還在（多半在卡片與 modal 內距），建議收成 12 / 12 / 24 / 32。這一項對視覺影響最小，優先度最低。
10. **深色底的紅色變體。** `{colors.primary-on-dark}` 已經定義好，但目前深色區塊裡還沒有紅字可以套用；之後在登入頁或深色卡片加連結時要記得用它。
11. **觸控尺寸。** 列內的 ghost 按鈕仍是 7px × 14px 內距，行動版要放大到 44px 的點擊區。

## 待補 Known gaps

- 空狀態（搜尋無結果、尚未借閱任何書）在現有畫面沒有設計，只有一行文字。這是最該補的一塊。
- 載入中與骨架屏沒有定義。
- 表格排序、分頁、批次選取都還沒出現，一旦館藏超過兩百筆就會需要。
- 深色模式沒有對應版本。若要做，`{colors.canvas}` → `#141516`、`{colors.surface}` → `#1C1C1C`、細線 → `#2A2C2E`，動作色換 `{colors.primary-on-dark}`。
- 逾期罰款（介面上出現過 NT$10/日）沒有完整的計費與提示規則。
- 圖示系統尚未定義，目前所有圖示位置都是幾何方塊與圓點。挑定一套之後要補上尺寸與線寬規則。

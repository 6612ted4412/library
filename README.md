# 承光圖書館

圖書館借閱系統的介面專案。讀者端可以查館藏、借書、歸還；管理端做借閱、書籍、使用者的管理。整個專案是**純前端的設計稿**：用 design-canvas 格式撰寫，經腳本建置成可以直接離線打開的單檔 HTML，不需要伺服器、資料庫或任何安裝步驟。

## 快速預覽

clone 下來之後，用瀏覽器打開 **`preview/index.html`** 就能看到全部畫面的總覽，包含三個入口：

| 畫面 | 檔案 | 內容 |
|---|---|---|
| 讀者端 Patron Portal | `preview/Patron_Portal.html` | 館藏查詢、我的借閱；支援訪客模式與登入 |
| 管理端 Library System | `preview/Library_System.html` | 借閱管理、書籍管理、使用者管理；含登入頁 |
| 線框稿 Wireframes | `preview/Wireframes.html` | 早期的排版方向探索（靜態頁） |

兩個主畫面是**可互動的**——搜尋、借書、歸還、切換分頁都能操作，資料是內建的示範資料（重新整理就重置）。右下角有一個半透明膠囊可以跳回總覽頁。

## 館規（所有畫面共用的商業邏輯）

- 每人同時最多借 **5 本**，借滿必須先歸還才能再借
- 每本借期 **14 天**，應還日 = 借出日 + 14
- 同一書名可以有多冊，可借數 = copies − 借出中的數量
- 示範資料把「今天」固定為 **2026-08-24**，逾期天數以此為基準

## 目錄結構

```
library/
├─ CLAUDE.md                 # Claude Code 的專案說明（啟動時自動載入）
├─ design/
│  └─ design-system.md       # 設計規範：色票、字級、間距、元件、Do/Don't
├─ source/                   # ★ 要改介面，改這裡
│  ├─ Library_System_dc.html
│  ├─ Patron_Portal_dc.html
│  ├─ Wireframes_dc.html
│  └─ originals/             # 對齊設計規範「之前」的原始匯出，純存檔勿動
├─ preview/                  # 由 source/ 建置產生的單檔預覽，不要手改
│  ├─ index.html             # 總覽頁（唯一手寫的預覽檔）
│  ├─ Library_System.html
│  ├─ Patron_Portal.html
│  └─ Wireframes.html
└─ tools/
   ├─ build_preview.py       # source/ → preview/
   ├─ refactor.py            # 把 source/ 對齊設計規範
   └─ dc-runtime.js          # 預覽用的極簡樣板執行環境（會被內嵌進預覽檔）
```

## 修改流程

1. 編輯 `source/` 裡的 `*_dc.html`
2. 建置預覽：

   ```bash
   python3 tools/build_preview.py    # 產生 preview/ 三個單檔 HTML
   ```

3. 打開 `preview/` 對應的檔案確認效果

只需要 Python 3 標準函式庫，沒有其他相依。`preview/` 完全可以由 `source/` 重建，所以**永遠不要直接改 preview/**（唯一例外是手寫的 `index.html`）。

另有一支一次性的整理腳本：

```bash
python3 tools/refactor.py    # 字級收斂、圓角收斂、紅字對比、補過場與焦點樣式
```

它會就地改寫 `source/` 的兩個互動畫面並印出變更統計，只在需要把手寫樣式重新對齊規範時才跑。

## source 檔的格式（design-canvas）

`*_dc.html` 是設計稿格式，重點只有幾個：

- `<helmet>…</helmet>` — 會被放進預覽檔 `<head>` 的字型與樣式
- `<x-dc>…</x-dc>` — 畫面樣板本體
- `{{ state.某值 }}` — 資料綁定；`<sc-if>`、`<sc-for>` — 條件與迴圈
- `onClick` / `onChange`、`style-hover` — 互動與懸停樣式
- `<script type="text/x-dc">` — 畫面的狀態與邏輯（`Component` 類別，`setState` 驅動重繪）

建置時 `build_preview.py` 會把樣板、邏輯和 `dc-runtime.js` 打包成一個獨立 HTML；線框稿沒有邏輯，直接輸出靜態頁。

## 設計規範

完整規範在 **`design/design-system.md`**：骨架取自 Apple 的網頁規範（單一動作色、表面換色代替裝飾、卡片用細線不用陰影、按下 scale(0.95)），動作色換成承光紅 `#DC2F33`，密度調整成後台系統需要的資料密度。改任何視覺之前先讀它。

最常違反的三條：

1. 紅色當**文字**用 `#B7262A`，當**底色**才用 `#DC2F33`；深色底上用 `#FF6B63`
2. 字級只用規範上的階梯，不要新增中間值（要新層次改字重或濃度，不是改字級）
3. 卡片用 1px `#E6E8EA` 細線、不加陰影；整套系統只有 toast 有陰影

## 已知待補

規範文件的「落差檢查／待補」章節有完整清單，前幾項：

- **空狀態**（搜尋無結果、尚未借書）目前只有一行文字，是最該補的一塊
- 載入中／骨架屏沒有定義
- 表格排序、分頁、批次選取尚未出現
- 深色模式沒有對應版本（色票已在規範裡預留）
- 圖示系統未定，目前以幾何方塊與圓點佔位

## 搭配 Claude Code

在 repo 根目錄執行 `claude`，`CLAUDE.md` 會自動載入——館規、目錄慣例和設計規範（透過 `@design/design-system.md` 匯入）都會直接進到 context，不用每次重貼。開場可以用 `/memory` 確認載入狀態，然後直接下指令，例如：

> 讀 design/design-system.md，然後幫我補空狀態

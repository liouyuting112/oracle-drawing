# 數位命理大師 2.0 (Digital Oracle Master)
此專案結合了東方靈籤、西方塔羅，並串接地端 H200 AI 模型進行深度諮商。

## 🛠️ 專案結構 (封裝說明)
本專案採用「前端-後端-資料庫」三層封裝架構：
- **`index.html`**：視覺美觀的前端介面 (HTML/JS/Tailwind)。
- **`server.py`**：核心後端代理 (FastAPI)。負責判斷 AI 調用時機，並實作 **API 防護「密封 (Seal)」**。
- **`master_db.json`**：收錄 2100+ 籤詩與 78 張塔羅牌的靜態資料庫。

## 🚀 快速啟動
1. **安裝環境**：
   ```bash
   pip install fastapi uvicorn slowapi requests aiohttp
   ```
2. **啟動後端**：
   ```bash
   python server.py
   ```
3. **開啟網頁**：直接點擊 `index.html`。

## 🧪 測試與驗證
- **極端壓力測試**：執行 `python stress_test.py` 驗證 API 防護是否能阻擋連續攻擊。
- **AI 地圖功能**：在提問框輸入「我要從台科大到台北101」，觀察 H200 是否能回傳正確座標與路線（此功能利用了 **台科大 AI 數位雙生實驗室** 之算力）。

## ⚠️ 安全注意事項
不要將 `server.py` 中的 H200 IP 直接暴露在公開網頁的原始碼中。本專案透過後端中繼，已將 IP 隱藏在伺服器端，使用者僅會看到您的後端位址。

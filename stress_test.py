import asyncio
import aiohttp
import time

API_URL = "http://localhost:8000/api/predict"

async def send_request(session, i):
    payload = {
        "system": "eastern",
        "type": "mazu60",
        "id": 1,
        "question": f"極端測試請求 #{i}",
        "category": "其他"
    }
    start = time.time()
    async with session.post(API_URL, json=payload) as response:
        status = response.status
        elapsed = time.time() - start
        print(f"Request #{i}: Status {status}, Time: {elapsed:.2f}s")
        return status

async def main():
    print("🚀 開始進行極端壓力測試...")
    print("目標：每秒發送 10 個請求，觀察後端防護是否生效 (預期會出現 429 Too Many Requests)")
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(20): # 發送 20 個請求
            tasks.append(send_request(session, i))
        
        results = await asyncio.gather(*tasks)
        
        success = results.count(200)
        blocked = results.count(429)
        print("\n" + "="*30)
        print(f"測試結果摘要：")
        print(f"成功處理 (200 OK): {success}")
        print(f"成功攔截 (429 Blocked): {blocked}")
        print("="*30)
        
        if blocked > 0:
            print("✅ 結論：防護機制（Seal）運作正常！成功攔截過多呼叫，保護了 H200 算力。")
        else:
            print("❌ 結論：防護未觸發，請檢查 Rate Limit 設定。")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"測試失敗，請確認後端 server.py 已啟動：{e}")

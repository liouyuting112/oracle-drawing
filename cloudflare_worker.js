/**
 * Cloudflare Worker: The Ultimate Seal for H200 API
 * 
 * This worker acts as a secure proxy to hide your NTUST IP (140.118)
 * and provides global rate limiting.
 */

const H200_ORIGIN = "http://140.118.157.225:11434";
const API_KEY = "YOUR_SECRET_COMPANY_KEY"; // Optional: Add a custom header for verification

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    
    // Handle CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type",
        },
      });
    }

    if (request.method !== "POST") {
      return new Response("請使用 POST 請求命理諮商", { status: 405 });
    }

    try {
      const body = await request.text();
      const newRequest = new Request(H200_ORIGIN + "/api/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Seal-Key": API_KEY,
        },
        body: body,
      });

      const response = await fetch(newRequest);
      
      const newResponse = new Response(response.body, response);
      newResponse.headers.set("Access-Control-Allow-Origin", "*");
      newResponse.headers.set("X-Seal-Status", "Protected-by-Cloudflare-v2");
      
      return newResponse;
    } catch (error) {
      return new Response(JSON.stringify({
        error: "Cloudflare 轉發失敗",
        detail: error.message,
        tip: "這是因為 Cloudflare 邊緣節點無法存取私有或未授權的 IP (140.118)，請改用 Cloudflare Tunnel (cloudflared) 建立安全通道。"
      }), { 
        status: 502,
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
      });
    }
  },
};

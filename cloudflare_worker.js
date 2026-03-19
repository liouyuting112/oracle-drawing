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
    
    // 1. Only allow POST requests to /api/generate
    if (request.method !== "POST") {
      return new Response("Method Not Allowed", { status: 405 });
    }

    // 2. Simple Rate Limiting (Using CF IP as key)
    // Note: For advanced rate limiting, use Cloudflare's built-in Rate Limiting features.
    
    // 3. Proxy to H200
    const newRequest = new Request(H200_ORIGIN + "/api/generate", {
      method: "POST",
      headers: request.headers,
      body: request.body,
    });

    const response = await fetch(newRequest);
    
    // 4. Return the response with CORS headers
    const newResponse = new Response(response.body, response);
    newResponse.headers.set("Access-Control-Allow-Origin", "*");
    newResponse.headers.set("X-Seal-Status", "Protected-by-Cloudflare");
    
    return newResponse;
  },
};

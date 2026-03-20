/**
 * Cloudflare Worker: Gemini API Secure Proxy
 * 
 * This worker acts as a secure middleman between your frontend and Google's Gemini API.
 * It hides your API Key and handles CORS, so you can safely deploy your tool 
 * on GitHub Pages or any other static platform.
 */

// IMPORTANT: In Cloudflare Dashboard, add these as Variables/Secrets:
// - GEMINI_API_KEY: Your actual Google API Key
// - GEMINI_MODEL: gemini-1.5-flash

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    
    // 1. Handle CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type",
          "Access-Control-Max-Age": "86400",
        },
      });
    }

    if (request.method !== "POST") {
      return new Response("Method Not Allowed. Please use POST for Oracle Consultation.", { status: 405 });
    }

    try {
      const body = await request.json();
      const prompt = body.prompt;

      if (!prompt) {
        return new Response(JSON.stringify({ error: "Missing prompt in request body" }), { 
          status: 400, 
          headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" } 
        });
      }

      // 2. Prepare request to Google Gemini API
      // Use env.GEMINI_API_KEY if defined in Cloudflare, otherwise fallback to a placeholder
      const apiKey = env.GEMINI_API_KEY || "YOUR_FALLBACK_KEY_IF_NOT_IN_ENV";
      const model = env.GEMINI_MODEL || "gemini-1.5-flash";
      const geminiUrl = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;

      const geminiRequest = {
        contents: [{ parts: [{ text: prompt }] }]
      };

      const response = await fetch(geminiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(geminiRequest),
      });

      const data = await response.json();

      // 3. Return clean response to frontend
      const interpretation = data.candidates?.[0]?.content?.parts?.[0]?.text || "大師正在冥想，目前無法給出回應。";

      return new Response(JSON.stringify({ interpretation }), {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          "X-Oracle-Status": "Guided-by-Gemini-via-Cloudflare"
        },
      });

    } catch (error) {
      return new Response(JSON.stringify({
        error: "Cloudflare Worker Error",
        detail: error.message
      }), { 
        status: 500,
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
      });
    }
  },
};

# 🏷️ ListingCraft

**AI Product Listing Generator for Small Sellers**

Turn rough product notes into polished, SEO-friendly marketplace listings — powered by open-weight AI.

## ✨ What It Does

Paste your rough product details → pick a platform (Etsy, eBay, Amazon) → get a polished listing with:
- Catchy title
- Compelling description
- Key feature bullet points
- SEO tags/keywords

## 🚀 Quick Start

```bash
# 1. Clone and install
git clone https://github.com/YOUR_USERNAME/listingcraft.git
cd listingcraft
pip install -r requirements.txt

# 2. Get a free Groq API key at https://console.groq.com/keys
export GROQ_API_KEY=your_key_here   # Linux/Mac
set GROQ_API_KEY=your_key_here      # Windows

# 3. Run
python app.py
```

Open http://localhost:7860 in your browser.

## 🤖 How It Works

ListingCraft uses **Llama 3** (Meta's open-weight model) via [Groq](https://groq.com)'s free inference API. The model is fully open-weight — meaning anyone can inspect, modify, or self-host it.

- **Model**: `meta-llama/llama-4-scout-17b-16e-instruct` (open-weight, Apache 2.0-like license)
- **Framework**: Gradio (open-source UI library)
- **No data stored** — your product details are sent to the model and forgotten

## 🔓 Why Open-Source AI?

- **No vendor lock-in** — swap Llama for Gemma, Mistral, or any open model
- **Free to run** — Groq's free tier is generous; or self-host the model yourself
- **Transparent** — the model weights are public, no black-box pricing surprises
- **Community-driven** — improvements come from thousands of contributors

## 📄 License

MIT — use it however you want.

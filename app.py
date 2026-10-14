"""
ListingCraft — AI Product Listing Generator for Small Sellers
Uses open-weight Llama 3 model via Groq (free API) to turn rough
product details into polished marketplace descriptions.
"""

import os
import gradio as gr
from groq import Groq

SYSTEM_PROMPT = """You are a product listing copywriter for online marketplaces like Etsy, eBay, and Amazon.

Given rough product details, generate a polished, SEO-friendly listing with:
1. A catchy title (max 80 chars)
2. A compelling description (2-3 short paragraphs)
3. 5 bullet-point key features
4. 5 suggested tags/keywords

Keep the tone friendly and professional. Highlight what makes the product special.
Format your response clearly with headers."""

PLATFORMS = ["Etsy", "eBay", "Amazon", "General Marketplace"]
TONES = ["Professional", "Casual & Friendly", "Luxury & Premium", "Fun & Quirky"]


def generate_listing(product_details: str, platform: str, tone: str) -> str:
    """Generate a polished product listing from rough details."""
    if not product_details.strip():
        return "⚠️ Please enter some product details first!"

    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        return (
            "⚠️ GROQ_API_KEY not set.\n\n"
            "Get a free key at https://console.groq.com/keys\n"
            "Then set it: export GROQ_API_KEY=your_key_here"
        )

    client = Groq(api_key=api_key)

    user_prompt = (
        f"Platform: {platform}\n"
        f"Tone: {tone}\n"
        f"Product details:\n{product_details}\n\n"
        "Generate a complete product listing."
    )

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
            max_tokens=1024,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}"


# --- Gradio UI ---
with gr.Blocks(
    title="ListingCraft",
    theme=gr.themes.Soft(),
) as app:
    gr.Markdown(
        "# 🏷️ ListingCraft\n"
        "*Turn rough product notes into polished marketplace listings — "
        "powered by open-weight AI (Llama 3)*"
    )

    with gr.Row():
        with gr.Column(scale=1):
            details = gr.Textbox(
                label="Product Details",
                placeholder=(
                    "e.g. Handmade ceramic mug, blue glaze, holds 12oz, "
                    "dishwasher safe, made in Portland..."
                ),
                lines=6,
            )
            platform = gr.Dropdown(PLATFORMS, value="Etsy", label="Platform")
            tone = gr.Dropdown(TONES, value="Professional", label="Tone")
            btn = gr.Button("✨ Generate Listing", variant="primary")

        with gr.Column(scale=1):
            output = gr.Markdown(label="Generated Listing")

    btn.click(generate_listing, inputs=[details, platform, tone], outputs=output)

    gr.Markdown(
        "---\n"
        "*Built with open-weight Llama 3 via Groq · No data stored · "
        "[GitHub](https://github.com) · Hacktoberfest 2026*"
    )

if __name__ == "__main__":
    app.launch()

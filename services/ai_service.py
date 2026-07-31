import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)


def generate_text(prompt):

    response = client.chat.completions.create(

        model="meta-llama/llama-3.3-70b-instruct",

        messages=[
            {
                "role": "system",
                "content": "You are a professional AI content creator for YouTube Shorts, TikTok and Instagram Reels."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7,
    )

    return response.choices[0].message.content


def summarize_text(text):

    response = client.chat.completions.create(

        model="meta-llama/llama-3.3-70b-instruct",

        messages=[
            {
                "role": "system",
                "content": "You are a professional document summarizer."
            },
            {
                "role": "user",
                "content": f"Summarize this document professionally:\n\n{text[:15000]}"
            }
        ],

        temperature=0.3,
    )

    return response.choices[0].message.content
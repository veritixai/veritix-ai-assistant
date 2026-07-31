import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)


def ask_pdf(question, text, history=None):

    messages = [
        {
            "role": "system",
            "content": """
You are Veritix AI.

Answer ONLY using the uploaded document.

If the answer is not found in the document, say:

'I couldn't find this information in the document.'
"""
        }
    ]

    if history:
        for chat in history:
            messages.append({
                "role": "user",
                "content": chat["question"]
            })

            messages.append({
                "role": "assistant",
                "content": chat["answer"]
            })

    messages.append({
        "role": "user",
        "content": f"""
Document:

{text[:15000]}

Question:

{question}
"""
    })

    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct",
        messages=messages,
        temperature=0.2,
    )

    return response.choices[0].message.content
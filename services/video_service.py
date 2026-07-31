from services.ai_service import generate_text


def generate_video_script(topic, style, duration):
    prompt = f"""
You are a professional YouTube Shorts script writer.

Create a {duration} script.

Topic:
{topic}

Style:
{style}

Rules:
- Hook in the first sentence.
- Short sentences.
- Engaging.
- End with a call to action.
- Return only the script.
"""

    return generate_text(prompt)
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_STYLE = """
You are a helpful AI assistant like ChatGPT.

You MUST follow these language rules:
- If the user writes in English → respond in English
- If the user writes in Kinyarwanda → respond in Kinyarwanda
- If mixed → respond in the same mixed style

Style rules:
- Be clear and structured
- Keep answers simple
- Use short paragraphs
- Be helpful and polite
"""

def get_response(message):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_STYLE},
                {"role": "user", "content": message}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
from groq import Groq

GROQ_API_KEY = "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"
LLM_MODEL = "llama-3.3-70b-versatile"

def get_response(messages, mode="Concise"):
    try:
        client = Groq(api_key=GROQ_API_KEY)
        tone = "Be concise. Max 3 sentences." if mode == "Concise" else "Be thorough and detailed."
        system = {"role": "system", "content": tone}
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[system] + messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
import openai

openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

def open_ia_response(prompt):
    response = openai.ChatCompletion.create(
        model="openai/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

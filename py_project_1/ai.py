from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyA1YNC3rB7p_bVoL5ShB64QDLlBrQQhxsM",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant named jarvis like chatgpt and gemini and keep the response 3 lines."},
        {"role": "user","content": "Who is ironman"}
    ]
)

print(response.choices[0].message.content)

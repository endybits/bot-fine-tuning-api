import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_bot_response(message: str = ""):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant"},
            {"role": "user", "content": "What is AI?"},
            {"role": "assistant", "content": "AI is Artificial Inteligence"},
            {"role": "user", "content": "When can I use LLM models?"}

        ],
        max_tokens=500,
        temperature=0,
        n=1,
        stream=True,
        )
    return response


async def chat_streamer():
    response = get_bot_response("When can I use LLM models?")
    for chunk in response:
        if chunk.choices[0].delta.get("content"):
            yield f"{chunk.choices[0].delta.content}"
            print(chunk.choices[0].delta.content, end="")
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from chat_ai import chat_streamer

app = FastAPI()


@app.get('/')
def home():
    return "Hello World"


@app.get('/chat')
def chat_conversation():
    return StreamingResponse(chat_streamer())


if __name__ == '__main__':
    uvicorn.run(app=app)
from fastapi import FastAPI

from model_loader import ModelLoader

app = FastAPI(title="Emotion-Aware Chatbot API", version="0.1.0")
model_loader = ModelLoader()


@app.on_event("startup")
async def startup_event() -> None:
    model_loader.load()


@app.get("/health")
async def health_check() -> dict:
    return {"status": "ok"}

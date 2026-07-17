from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.analytics import router as analytics_router

app = FastAPI(
    title="AI Conversational Analytics Assistant",
    version="1.0.0",
    description="AI Powered Business Analytics System"
)

app.include_router(chat_router)
app.include_router(analytics_router)


@app.get("/")
def home():

    return {
        "message": "AI Conversational Analytics Assistant",
        "status": "Running"
    }
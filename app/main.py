from fastapi import FastAPI
from app.routes import health, text_summarization

app = FastAPI(title="Text-to-talk API")

# Include routers without schemas or complex structure
app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(text_summarization.router, prefix="/api",
                   tags=["text summarization"])

# Run the app with `uvicorn app.main:app --reload`

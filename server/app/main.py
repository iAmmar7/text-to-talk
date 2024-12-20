from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import health, text_summarization, text_to_speech, summarize_to_speech

app = FastAPI(title="Text-to-talk API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all HTTP headers
)

# Include routers without schemas or complex structure
app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(text_summarization.router, prefix="/api",
                   tags=["text summarization"])
app.include_router(text_to_speech.router, prefix="/api",
                   tags=["text to speech"])
app.include_router(summarize_to_speech.router,
                   prefix="/api", tags=["summarize to speech"])


# Run the app with `uvicorn app.main:app --reload`

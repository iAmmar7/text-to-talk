from fastapi import APIRouter, HTTPException
from transformers import pipeline
from app.schemas import TextSummarizationRequest

# Initialize the summarization pipeline using a BART model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Create a router for the text summarization API
router = APIRouter()


@router.post("/summarize")
async def summarize_text(request: TextSummarizationRequest):
    """
    Summarize the provided text using the Facebook's BART model.
    - `text`: The input text to summarize.
    - `min_length`: Minimum length of the summary (optional).
    - `max_length`: Maximum length of the summary (optional).
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text must not be empty.")

    # Validate that min_length does not exceed max_length
    if request.min_length > request.max_length:
        raise HTTPException(
            status_code=400,
            detail="`min_length` cannot be greater than `max_length`."
        )

    try:
        # Validate that min_length and max_length are within input length
        input_length = len(request.text.split())
        min_length = min(request.min_length, input_length)
        max_length = min(request.max_length, input_length)

        # Generate the summary with the validated min_length and max_length
        summary = summarizer(
            request.text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An error occurred: {str(e)}")

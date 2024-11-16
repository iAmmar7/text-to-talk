from transformers import AutoProcessor, AutoModel
from fastapi import APIRouter, HTTPException, Response, Depends
from app.schemas import TextSummarizationRequest
from transformers import pipeline
from io import BytesIO
import scipy

# Initialize components
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
processor = AutoProcessor.from_pretrained("suno/bark")
model = AutoModel.from_pretrained("suno/bark")

# Create a router for the summarize to speech API
router = APIRouter()


@router.post("/summarize-to-speech")
async def summarize_to_speech(request: TextSummarizationRequest):
    """
    Summarize the provided text and convert the summary to speech.
    - `text`: The input text to summarize and convert to speech.
    - `min_length`: Minimum length of the summary (optional).
    - `max_length`: Maximum length of the summary (optional).
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text must not be empty.")

    # Summarization Step
    try:
        input_length = len(request.text.split())
        min_length = min(request.min_length, input_length)
        max_length = min(request.max_length, input_length)

        summary = summarizer(
            request.text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )[0]['summary_text']
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An error occurred during summarization: {str(e)}")

    # Text-to-Speech Step
    try:
        # Generate speech from summarized text
        inputs = processor(text=summary, return_tensors="pt")
        speech_output = model.generate(**inputs, do_sample=True)

        # Store audio in a buffer
        audio_buffer = BytesIO()
        scipy.io.wavfile.write(audio_buffer, rate=24000,
                               data=speech_output.cpu().numpy().squeeze())
        audio_buffer.seek(0)  # Reset buffer pointer to the beginning

        # Return the buffer content as a WAV response
        return Response(content=audio_buffer.read(), media_type="audio/wav")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An error occurred during TTS generation: {str(e)}")

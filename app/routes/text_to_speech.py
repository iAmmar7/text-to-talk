from fastapi import APIRouter, HTTPException, Response
from transformers import AutoProcessor, AutoModel
import scipy
from io import BytesIO
from app.schemas import TextToSpeechRequest

processor = AutoProcessor.from_pretrained("suno/bark")
model = AutoModel.from_pretrained("suno/bark")

# Create a router for the text summarization API
router = APIRouter()


@router.post("/text-to-speech")
async def text_to_speech(request: TextToSpeechRequest):
    """
    Convert the provided text to speech using the Bark model.
    - `text`: The input text to convert to speech.
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text must not be empty.")

    try:
        # Generate speech from text
        inputs = processor(text=request.text, return_tensors="pt")

        speech_output = model.generate(**inputs, do_sample=True)

        # Store audio in a buffer instead of saving to a file
        audio_buffer = BytesIO()
        scipy.io.wavfile.write(audio_buffer, rate=24000,
                               data=speech_output.cpu().numpy().squeeze())
        audio_buffer.seek(0)  # Reset buffer pointer to the beginning

        # Return the buffer content as a WAV response
        return Response(content=audio_buffer.read(), media_type="audio/wav")

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An error occurred during TTS generation: {str(e)}")

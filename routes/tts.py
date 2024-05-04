from flask import request, jsonify, send_file
from transformers import AutoProcessor, BarkModel
import scipy

# Load processor and model from Hugging Face
processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")

model.to("cpu")  # Using CPU here as CUDA is not enabled

def text_to_speech():
    if not request.is_json:
        return jsonify({ "error": "Request must be JSON" }), 400

    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data['text']
    preset = "v2/en_speaker_9"
    output = "output.wav"

    input = processor(text, voice_preset=preset)
    input = {k: v.to("cpu") for k, v in input.items()}  # Move all tensors to CPU
    audio_array = model.generate(**input)
    audio_array = audio_array.cpu().numpy().squeeze()
    sample_rate = model.generation_config.sample_rate
    scipy.io.wavfile.write(output, rate=sample_rate, data=audio_array)

    # Return the audio file
    return send_file(output, as_attachment=True)

    # return jsonify({ "response": text })

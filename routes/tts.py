from flask import request, jsonify, send_file
from transformers import AutoProcessor, AutoModelForTextToWaveform
import scipy

# Load processor and model from Hugging Face
processor = AutoProcessor.from_pretrained("suno/bark")
model = AutoModelForTextToWaveform.from_pretrained("suno/bark")


def text_to_speech():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data['text']
    voice_preset = "v2/en_speaker_6"

    inputs = processor(text, voice_preset=voice_preset)

    audio_array = model.generate(**inputs)
    audio_array = audio_array.cpu().numpy().squeeze()

    sample_rate = model.generation_config.sample_rate
    output = "output.wav"

    scipy.io.wavfile.write(output, rate=sample_rate, data=audio_array)

    # Return the audio file
    return send_file(output, as_attachment=True)

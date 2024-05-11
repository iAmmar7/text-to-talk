from flask import request, jsonify, send_file
from transformers import AutoProcessor, BarkModel
import scipy

# Load processor and model from Hugging Face
processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")


def text_to_speech():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data['text']
    voice_preset = "v2/en_speaker_6"

    # Process the input text with a specific voice preset to prepare it for the model.
    inputs = processor(text, voice_preset=voice_preset)

    # Generate audio from the processed input using the model.
    audio_array = model.generate(**inputs)

    # Move the generated audio tensor to CPU, convert to NumPy array, and remove extra dimensions.
    audio_array = audio_array.cpu().numpy().squeeze()

    # Retrieve the sample rate for the generated audio from the model's configuration.
    sample_rate = model.generation_config.sample_rate
    output = "output.wav"

    scipy.io.wavfile.write(output, rate=sample_rate, data=audio_array)

    # Return the audio file
    return send_file(output, as_attachment=True)

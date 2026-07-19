from flask import Flask, render_template, request, jsonify, send_file
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from gtts import gTTS
import io

# Make language detection give the same result every time for the same text
DetectorFactory.seed = 0

app = Flask(__name__)

# Build {language_name: language_code} dict once at startup, e.g. {"english": "en", ...}
LANGUAGES = GoogleTranslator().get_supported_languages(as_dict=True)
CODE_TO_NAME = {code: name.title() for name, code in LANGUAGES.items()}
VALID_CODES = set(LANGUAGES.values())


@app.route("/")
def index():
    # Pass languages sorted alphabetically to the template for the dropdown
    sorted_languages = sorted(LANGUAGES.items())
    return render_template("index.html", languages=sorted_languages)


@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = (data.get("text") or "").strip()
    target = data.get("target", "en")

    if not text:
        return jsonify({"error": "Please enter some text to translate."}), 400

    # Detect the source language automatically -- the user no longer picks it
    try:
        detected_code = detect(text)
    except Exception:
        detected_code = None

    # langdetect's codes mostly match Google's, but not always.
    # If it's not a code Google Translate recognizes, let Google auto-detect instead.
    source_for_api = detected_code if detected_code in VALID_CODES else "auto"

    try:
        translated = GoogleTranslator(source=source_for_api, target=target).translate(text)
        detected_name = CODE_TO_NAME.get(detected_code, "Detected automatically")
        return jsonify({
            "translated_text": translated,
            "detected_language": detected_name,
            "detected_code": detected_code or "auto",
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/speak", methods=["POST"])
def speak():
    """Generate real spoken audio for the given text using Google TTS,
    so pronunciation is correct for the actual language (not the browser's
    limited built-in voices)."""
    data = request.get_json()
    text = (data.get("text") or "").strip()
    lang = data.get("lang", "en")

    if not text:
        return jsonify({"error": "No text to speak."}), 400

    try:
        tts = gTTS(text=text, lang=lang)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return send_file(audio_buffer, mimetype="audio/mpeg")
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)

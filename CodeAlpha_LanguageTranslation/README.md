# CodeAlpha_LanguageTranslationTool

A simple web-based Language Translation Tool built with **Flask** (backend) and **HTML/CSS/JS** (frontend).
It uses the `deep-translator` library (Google Translate backend) — no API key required.

## Features
- Enter text and pick source & target languages (133 languages supported)
- Auto-detect source language option
- Swap source/target languages with one click
- Copy translated text to clipboard
- Text-to-speech playback of the translation (via browser's built-in speech synthesis)

## Project Structure
```
CodeAlpha_LanguageTranslationTool/
├── app.py                # Flask backend
├── templates/
│   └── index.html        # Frontend UI
├── requirements.txt
└── README.md
```

## Setup & Run (in VS Code)

1. Open this folder in VS Code.
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open your browser at **http://127.0.0.1:5000**

## Notes
- This project uses `deep-translator`'s `GoogleTranslator`, which is free and doesn't need an API key —
  a good substitute for the official Google Translate/Microsoft Translator APIs mentioned in the task,
  which require billing setup. If you'd rather use the official Google Cloud Translation API, you can
  swap out the translation call in `app.py` for `google-cloud-translate` and add your API key.
- Requires an internet connection (it calls Google Translate's public endpoint under the hood).

## Submission Checklist (per CodeAlpha instructions)
- [ ] Push this folder to a GitHub repo named `CodeAlpha_LanguageTranslationTool`
- [ ] Record a short video walkthrough and post it on LinkedIn, tagging @CodeAlpha
- [ ] Submit via the CodeAlpha submission form

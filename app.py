#!/usr/bin/env python3
import os
import uuid
from flask import Flask, request, jsonify, send_from_directory, render_template

from translator import translate_text, text_to_speech_kannada

APP_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_AUDIO_DIR = os.path.join(APP_DIR, 'static', 'audio')
os.makedirs(STATIC_AUDIO_DIR, exist_ok=True)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/translate', methods=['POST'])
def api_translate():
    data = request.get_json() or {}
    text = data.get('text', '').strip()
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        translated = translate_text(text)
        fname = f"{uuid.uuid4().hex}.mp3"
        out_path = os.path.join(STATIC_AUDIO_DIR, fname)
        text_to_speech_kannada(translated, out_path)
        audio_url = f"/static/audio/{fname}"
        return jsonify({'translated': translated, 'audio': audio_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Allow overriding port and debug via environment variables for flexibility
    port = int(os.environ.get('PORT', '5000'))
    debug_env = os.environ.get('FLASK_DEBUG')
    if debug_env is None:
        debug = True
    else:
        debug = debug_env.lower() in ('1', 'true', 'yes')
    app.run(host='0.0.0.0', port=port, debug=debug)

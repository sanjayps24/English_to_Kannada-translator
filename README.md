# English → Kannada Translator + Text-to-Speech

Simple CLI tool to translate English text into Kannada and generate speech (MP3) using `googletrans` and `gTTS`.

Prerequisites
- Python 3.8+
- Internet connection (translation and TTS use online services)

Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Usage

- Translate a phrase and save speech:

```bash
python3 translator.py "Hello, how are you?" -o hello_kn.mp3
```

- Read from stdin:

```bash
echo "Good morning" | python3 translator.py -o morning_kn.mp3
```

- Automatically open the resulting MP3 (Linux desktops with `xdg-open`):

```bash
python3 translator.py "See you later" -o later_kn.mp3 --play
```
-
Web UI

Start the web app and open a browser at http://localhost:5000:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Enter English text into the page, click the button, and the page will display the Kannada translation and an audio player.

Notes
- This uses `googletrans` and `gTTS`, both require network access.
- If `xdg-open` is not available, open the MP3 file in your preferred media player.

Next steps
- Add a small web UI or packaging into a desktop app on request.
# English_to_Kannada-translator
Translate English text to Kannada text and speech



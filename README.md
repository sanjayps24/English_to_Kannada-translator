# 🌐 English to Kannada Translator
##    (Text & Speech Based Language Translation System)

A simple yet powerful translator that converts English text and speech into Kannada, making communication easier, faster, and more inclusive.

 This project is live and deployed using Render 
 https://english-to-kannada-translator-wce4.onrender.com/

## 🚀 Project Overview

- Language should never be a barrier.

- This project provides a user-friendly translation system that supports:

- 📝 Text Translation (English → Kannada)

- 🎙 Speech-to-Text Translation

- 🔊 Text-to-Speech Output in Kannada

- It is designed to help students, travelers, native Kannada speakers, and anyone learning regional languages.

## ✨ Features

 - ✅ English to Kannada Text Translation
 - ✅ English Speech Recognition
 - ✅ Kannada Text-to-Speech Output
 - ✅ Simple & Interactive UI
 - ✅ Fast and Accurate Results
 - ✅ Beginner-friendly & Scalable Design

## 🛠️ Tech Stack Used

 * Technology	Purpose
 * Programming Language	 -   Python 
 * Translation API	     -   Google Translate API / Custom Model
 * Speech Recognition	 -   Speech-to-Text API
 * Text-to-Speech	     -   TTS Engine
 * Frontend	             -   HTML / CSS / JavaScript
 * Backend	             -   python(Flask) 

## 🧠 How It Works (Simple Flow)

    User Input
         ↓
    English Text / Speech
         ↓
    Speech-to-Text (if speech input)
         ↓
    Translation Engine
         ↓
    Kannada Text Output
         ↓
    Text-to-Speech (Optional)

## 🎯 Use Cases

- 📚 Language learning & practice

- 🏫 Educational institutions

- 🏥 Public service communication

- 🧳 Travelers & tourists

- 🗣 Helping non-English speakers




## 🧪 Example Usage

    Text Translation
    Input: "Good Morning"
    Output: "ಶುಭೋದಯ"

### Speech Translation

    🎙 Speak: "How are you?"
    📢 Output: "ನೀವು ಹೇಗಿದ್ದೀರಾ?"

## ⚙️ Installation & Setup

Step 1: Clone the Repository git clone https://github.com/your-username/english-to-kannada-translator.git

Step 2: Install Dependencies

    pip install -r requirements.txt

Step 3: Run the Application

    python app.py


## 🔮 Future Enhancements

🌍 Support for multiple Indian languages

📱 Mobile application version

🤖 Offline translation using ML models

🎧 Noise filtering for better speech recognition

🧠 AI-powered context-based translation

## 🧑‍💻 Learning Outcomes

Through this project, I learned:

  1. Language translation workflows

  2. Speech-to-text & text-to-speech integration

  3. API handling & error management

  4. Real-world problem solving

  5. Clean and modular code design

## 🤝 Contributing

Contributions are welcome!
Feel free to:

Fork the repo

Create a feature branch

Submit a pull request

## 📜 License

This project is licensed under the MIT License.
You’re free to use, modify, and distribute it.

⭐ Final Note

“Technology is powerful when it connects people.”


## For LInux OS

### English → Kannada Translator + Text-to-Speech

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



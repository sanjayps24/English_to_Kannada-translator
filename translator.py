#!/usr/bin/env python3
import argparse
import subprocess
import sys
import asyncio

from gtts import gTTS

try:
    from googletrans import Translator
except Exception:
    Translator = None


def translate_text(text: str) -> str:
    if Translator is None:
        raise RuntimeError('googletrans is not installed')
    t = Translator()
    try:
        res = t.translate(text, src='en', dest='kn')
        # some installations provide an async translate (returns coroutine)
        if asyncio.iscoroutine(res):
            res = asyncio.run(res)

        # If result is an object with .text attribute
        if hasattr(res, 'text'):
            return res.text

        # If result is a dict-like
        if isinstance(res, dict):
            for key in ('text', 'translatedText', 'translation'):
                if key in res:
                    return res[key]
            # fallback to stringifying
            return str(res)

        # If result is a list, try first element
        if isinstance(res, (list, tuple)) and res:
            first = res[0]
            if hasattr(first, 'text'):
                return first.text
            if isinstance(first, dict):
                for key in ('text', 'translatedText', 'translation'):
                    if key in first:
                        return first[key]
            return str(first)

        return str(res)
    except Exception as exc:
        raise RuntimeError(f'Translation failed: {exc}') from exc


def text_to_speech_kannada(text: str, out_path: str) -> None:
    tts = gTTS(text=text, lang='kn')
    tts.save(out_path)


def main():
    parser = argparse.ArgumentParser(description='English → Kannada translator + TTS')
    parser.add_argument('text', nargs='*', help='Text to translate (if empty, read from stdin)')
    parser.add_argument('-o', '--output', default='output_kn.mp3', help='Output MP3 filename')
    parser.add_argument('--play', action='store_true', help='Open the output file after creation with xdg-open')
    args = parser.parse_args()

    if args.text:
        src_text = ' '.join(args.text)
    else:
        src_text = sys.stdin.read().strip()

    if not src_text:
        print('No input provided. Provide text as arguments or via stdin.', file=sys.stderr)
        sys.exit(1)

    try:
        print('Translating...')
        translated = translate_text(src_text)
        print('Kannada:', translated)

        print('Generating speech...')
        text_to_speech_kannada(translated, args.output)
        print('Saved:', args.output)

        if args.play:
            try:
                subprocess.run(['xdg-open', args.output], check=False)
            except Exception:
                print('Could not open file automatically.')
    except Exception as e:
        print('Error:', e, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

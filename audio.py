import json
import os
from datetime import datetime

from TTS.api import TTS
from pydub import AudioSegment

from text import Script

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cpu")


def generate_audio():
    print("Synthesizing audio...")
    script = Script(**json.loads(open("example_data/script.json").read()))
    temp_files = []
    output_file = "example_data/audio.wav"

    for i, phrase in enumerate(script.phrases):
        temp_files.append(tts.tts_to_file(text=phrase.phrase, speaker=phrase.speaker, language="en", speed=2,
                                          file_path=f"phrase_{i}.wav"))
    merge_audio_phrases(temp_files, output_file)
    print(f"Audio file saved at {output_file}")


def merge_audio_phrases(files: list[str], output_file: str):
    combined = AudioSegment.empty()

    for file in files:
        audio = AudioSegment.from_wav(file)
        combined += audio
        os.remove(file)

    combined.export(output_file, format="wav")


if __name__ == "__main__":
    generate_audio()

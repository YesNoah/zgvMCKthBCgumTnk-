

# Import modules
import subprocess
import os
import shutil
import whisper
from pathlib import Path
my_env = os.environ.copy()
my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
os.chdir(os.getcwd())
os.getcwd()




file_path = "data/noah_voice_train.wav"
model = whisper.load_model("base")
my_text = model.transcribe(file_path)["text"]



subprocess.Popen(
    F'tts  --text "{my_text}" --out_path data/testing/test1.wav --model_name tts_models/multilingual/multi-dataset/your_tts  --speaker_wav data/combined_wavs/DR1C/MRSO0.wav --language_idx "en"', env=my_env).wait()



import subprocess, os
from pathlib import Path
import random
my_env = os.environ.copy()
my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
my_text = "Seven sons of Lawyers, Inheiritors and their pillars of salt, monitor this glistening mecca with mute terrorism."
path_to_DR = 'data\combined_wavs\DR4C'
path_to_wav = 'data\combined_wavs\DR4C\MRGM0.wav'

def gen_speaker(DR = input("Region (DR1-DR8):"), speaker_name = input("Speaker(XXXXx):"), my_text = input("Text to be synthesized:")):
    #DR = Path(path_to_DR).stem
    #speaker_name = Path(path_to_wav).stem

    print(speaker_name)
    print(DR)
    if DR == "Random" or "random" or "r" or "R":
        DR = random.sample(os.listdir("data/combined_wavs/"),k=1)[0]
    else: DR == DR +"C"
    if speaker_name == "Random" or "random" or "r" or "R":
        speaker_name =str(Path(random.sample(os.listdir(F"data/combined_wavs/{DR}"),k=1)[0]).stem)
    else: speaker_name = speaker_name
    print(speaker_name)
    print(DR)
    input_path_ = F"data/combined_wavs/{DR}/{speaker_name}.wav"
    output_path_ = F"data/combined_wavsAI/outs/AI_{DR}_{speaker_name}.wav"

    subprocess.Popen(F'tts  --text "{my_text}" --out_path {output_path_} --model_name tts_models/multilingual/multi-dataset/your_tts  --speaker_wav {input_path_} --language_idx "en"', env=my_env)

gen_speaker()
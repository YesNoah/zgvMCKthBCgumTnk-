# Import modules
import subprocess
import os
import shutil
import whisper
from pathlib import Path
# Define a function that takes an input filepath and output filepath as arguments
my_env = os.environ.copy()
my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
os.chdir(os.getcwd())
os.getcwd()


def synthesize_wav_files(input_path, output_path):
    # Create the output directory if it does not exist
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    # Initialize an empty list to store the wav files
    _mp3_files = []
    # Loop through the files in the subsubdirectory
    for file in os.listdir(input_path):
        # Get the full path of the file
        file_path = os.path.join(input_path, file)

        # Check if it is a file and has .wav extension
        if os.path.isfile(file_path) and file.endswith(".mp3"):
            # Append it to the wav files list
            _mp3_files.append(file)

        # Sort the wav files list alphabetically (optional)
    _mp3_files.sort()
   
    # Loop through the wav files list
    for file in _mp3_files:
        print(F"mp3_file: {file}")

        speaker_name = Path(file).stem
        new_file = "AI" + file
        file_path = os.path.join(input_path, file)
        model = whisper.load_model("base")
        my_text = model.transcribe(file_path)["text"]
        output_path_ = os.path.join(output_path, new_file)
        print(F"output_path_: {output_path_}")

        subprocess.Popen(
            F'tts  --text "{my_text}" --out_path {output_path_} --model_name tts_models/multilingual/multi-dataset/your_tts  --speaker_wav {file_path} --language_idx "en"', env=my_env).wait()



# Use the __init__ statement to run the commands when the module is imported
if __name__ == "__main__":
    synthesize_wav_files(input_path=os.path.join(os.path.dirname(os.getcwd()), "VC_Repo\\data\\raw\\cv_delta\\clips"),
                         output_path=os.path.join(os.path.dirname(os.getcwd()), "VC_Repo\\data\\raw\\cv_delta\\AIclips"))

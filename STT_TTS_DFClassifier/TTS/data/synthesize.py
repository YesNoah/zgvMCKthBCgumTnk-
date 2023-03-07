# Import modules
import subprocess, os
import shutil

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

    # Loop through the subdirectories in the input path (DR1-DR8)
    for subdir in os.listdir(input_path):
        # Get the full path of the subdirectory
        subdir_path = os.path.join(input_path, subdir)
        # Check if it is a directory and has DR in its name
        if os.path.isdir(subdir_path) and "DR" in subdir:
            # Create a new subdirectory in the output path with AI appended to its name (DR1C-DR8C)
            DR = Path(subdir_path).stem
            new_subdir = subdir + "AI"
            print(F'new_subdir:{new_subdir}')
            new_subdir_path = os.path.join(output_path, new_subdir)
            os.makedirs(new_subdir_path, exist_ok=True)

            
            # Initialize an empty list to store the wav files
            _wav_files = []
            # Loop through the files in the subsubdirectory
            for file in os.listdir(subdir_path):
                # Get the full path of the file
                file_path = os.path.join(subdir_path, file)
                
                # Check if it is a file and has .wav extension
                if os.path.isfile(file_path) and file.endswith(".wav"):
                    # Append it to the wav files list
                    _wav_files.append(file)
                
            

            # Sort the wav files list alphabetically (optional)
            _wav_files.sort()

            # Loop through the wav files list 
            for wav_file in _wav_files:
                print(F"wav_file: {wav_file}")
                speaker_name = Path(wav_file).stem
                new_file = "AI" + wav_file
                output_path_ = os.path.join(new_subdir_path, new_file)
                print(F"output_path_: {output_path_}")
                my_text = ("She had your dark suit and greasy washwater all year. "
                           "Don't ask me to carry an oily rag like that. "
                           "Production may fall far below expectations. "
                           "His captain was thin an haggard and his beautiful boots were worn and shabby. "
                           "The reasons for this dive seemed foolish now. "
                           "Elderly people are often excluded. "
                           "Pizzerias are convenient for a quick lunch. " 
                           "Put the butcher block table in the garage. "
                           "Drop five forms in the box before you go out. "
                           "Her wardrobe consists of only skirts and blouses.")
                
                subprocess.Popen(F'tts  --text "{my_text}" --out_path {output_path_} --model_name tts_models/multilingual/multi-dataset/your_tts  --speaker_wav data/combined_wavs/{DR}/{speaker_name}.wav --language_idx "en"', env=my_env).wait()


            

# Use the __init__ statement to run the commands when the module is imported
if __name__ == "__main__":
    synthesize_wav_files(input_path='data\combined_wavs', output_path = 'data\combined_wavsAI')


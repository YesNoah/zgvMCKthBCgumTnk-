# Import modules
import os
import shutil
from pydub import AudioSegment

# Define a function that takes an input filepath and output filepath as arguments
def combine_wav_files(input_path, output_path):
    # Create the output directory if it does not exist
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    # Loop through the subdirectories in the input path (DR1-DR8)
    for subdir in os.listdir(input_path):
        # Get the full path of the subdirectory
        subdir_path = os.path.join(input_path, subdir)
        # Check if it is a directory and has DR in its name
        if os.path.isdir(subdir_path) and "DR" in subdir:
            # Create a new subdirectory in the output path with C appended to its name (DR1C-DR8C)
            new_subdir = subdir + "C"
            new_subdir_path = os.path.join(output_path, new_subdir)
            os.makedirs(new_subdir_path, exist_ok=True)

            # Loop through the subsubdirectories in the subdirectory (XXXXx)
            for subsubdir in os.listdir(subdir_path):
                # Get the full path of the subsubdirectory
                subsubdir_path = os.path.join(subdir_path, subsubdir)
                # Check if it is a directory and has four capital letters followed by a number in its name
                if os.path.isdir(subsubdir_path) and len(subsubdir) == 5 and subsubdir[:4].isupper() and subsubdir[-1].isdigit():
                    # Initialize an empty list to store the wav files
                    wav_files = []
                    # Loop through the files in the subsubdirectory
                    for file in os.listdir(subsubdir_path):
                        # Get the full path of the file
                        file_path = os.path.join(subsubdir_path, file)
                        # Check if it is a file and has .wav extension
                        if os.path.isfile(file_path) and file.endswith(".wav"):
                            # Append it to the wav files list
                            wav_files.append(file)

                    # Sort the wav files list alphabetically (optional)
                    wav_files.sort()

                    # Initialize an empty audio segment object to store the combined audio data
                    combined_audio = AudioSegment.empty()

                    # Loop through the wav files list 
                    for wav_file in wav_files:
                        # Get the full path of each wav file 
                        wav_file_path = os.path.join(subsubdir_path, wav_file)
                        # Load it as an audio segment object using pydub 
                        audio_segment = AudioSegment.from_wav(wav_file_path)
                        # Append it to the combined audio object with 0.5 second pause between them 
                        combined_audio += audio_segment + AudioSegment.silent(duration=200)

                    # Get the name of each combined audio file as XXXXx.wav 
                    combined_audio_name = subsubdir + ".wav"
                    # Get the full path of each combined audio file in the new subdirectory 
                    combined_audio_path = os.path.join(new_subdir_path, combined_audio_name)
                    # Export it as a wav file using pydub 
                    combined_audio.export(combined_audio_path, format="wav")

# Use the __init__ statement to run the commands when the module is imported
if __name__ == "__main__":
    # Call the function with both input paths and the same output path
    combine_wav_files("data/TEST", "data/combined_wavs")
    combine_wav_files("data/TRAIN", "data/combined_wavs")
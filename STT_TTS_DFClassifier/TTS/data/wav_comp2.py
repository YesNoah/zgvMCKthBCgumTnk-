# Import modules
import os
import shutil
from pydub import AudioSegment

# Define a function that takes a list of input paths and an output path as arguments
def combine_wav_files(input_paths, output_path):
    # Create the output directory if it does not exist
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    # Loop through the list of input paths (TRAIN and TEST)
    for input_path in input_paths:
        # Loop through the subdirectories in each input path (DR1-DR8)
        for subdir in os.listdir(input_path):
            # Get the full path of each subdirectory
            subdir_path = os.path.join(input_path, subdir)
            # Check if it is a directory and has DR in its name
            if os.path.isdir(subdir_path) and "DR" in subdir:
                # Create a new subdirectory in the output path with C appended to its name (DR1C-DR8C) if it does not exist 
                new_subdir = subdir + "C"
                new_subdir_path = os.path.join(output_path, new_subdir)
                if not os.path.exists(new_subdir_path):
                    os.mkdir(new_subdir_path)

                # Loop through the subsubdirectories in each subdirectory (XXXXx)
                for subsubdir in os.listdir(subdir_path):
                    # Get the full path of each subsubdirectory
                    subsubdir_path = os.path.join(subdir_path, subsubdir)
                    # Check if it is a directory and has four capital letters followed by a number in its name
                    if os.path.isdir(subsubdir_path) and len(subsubdir) == 5 and subsubdir[:4].isupper() and subsubdir[-1].isdigit():
                        # Initialize an empty list to store the wav files
                        wav_files = []
                        # Loop through the files in each subsubdirectory
                        for file in os.listdir(subsubdir_path):
                            # Get the full path of each file
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
                            # Append it to combined audio object with 0.5 second pause between them 
                            combined_audio += audio_segment + AudioSegment.silent(duration=500)

                        ## SIMPLIFIED CODE ##
                        
                        ## Export new one ##
                        
                        ## Get name of each combined audio file as XXXXx.wav 
                        combined_audio_name = subsubdir + ".wav"
                        
                        ## Get full path of each combined audio file in new subdirectory 
                        combined_audio_name_fullpath = f"{new_subdir}/{combined_audio_name}"
                        
                        
                        
                        
                        
                        
                        

                        ## Export new one ##
                        print(f"Exporting {combined_audio_name}...")
                        combined_audio.export(combined_audio_name_fullpath , format="wav")
                        print(f"Exported {combined_audio_name}.")
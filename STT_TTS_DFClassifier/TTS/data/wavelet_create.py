import subprocess, os
import shutil
from pathlib import Path
from pylab import *
import pywt
import scipy.io.wavfile as wavfile
os.environ['KMP_DUPLICATE_LIB_OK']='True'
# Define a function that takes an input filepath and output filepath as arguments
my_env = os.environ.copy()
my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]

# Find the highest power of two less than or equal to the input.
def lepow2(x):
    return 2 ** floor(log2(x))


# Make a scalogram given an MRA tree.
def scalogram(data):
    bottom = 0

    vmin = min(map(lambda x: min(abs(x)), data))
    vmax = max(map(lambda x: max(abs(x)), data))

    gca().set_autoscale_on(False)

    for row in range(0, len(data)):
        scale = 2.0 ** (row - len(data))

        imshow(
            array([abs(data[row])]),
            interpolation = 'nearest',
            vmin = vmin,
            vmax = vmax,
            extent = [0, 1, bottom, bottom + scale])

        bottom += scale

def generate_scaleograms(input_path, output_path):
    # Create the output directory if it does not exist
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    # Loop through the subdirectories in the input path (DR1-DR8)
    for subdir in os.listdir(input_path):
        # Get the full path of the subdirectory
        subdir_path = os.path.join(input_path, subdir)
        # Check if it is a directory and has DR in its name
        if os.path.isdir(subdir_path) and "DR" in subdir:
            _wav_files = []
            _wav_filepaths = []
            # Loop through the files in the subsubdirectory
            for file in os.listdir(subdir_path):
                # Get the full path of the file
                file_path = os.path.join(subdir_path, file)
                
                # Check if it is a file and has .wav extension
                if os.path.isfile(file_path) and file.endswith(".wav"):
                    # Append it to the wav files list
                    _wav_files.append(file)
                    _wav_filepaths.append(file_path)
                    # Sort the wav files list alphabetically (optional)
            
            

            # Loop through the wav files list 
            for wav_file, wav_filepath in zip(_wav_files,_wav_filepaths):
                print(F"wav_file: {wav_file}")
                speaker_name = Path(wav_file).stem
                new_file = "scale" + wav_file.split("/")[-1].replace(".wav",".png")
                output_path_ = os.path.join(output_path, new_file)
                print(F"output_path: {output_path_}")
                

                # Load the signal, take the first channel, limit length to a power of 2 for simplicity.
                rate, signal = wavfile.read(wav_filepath)
                output_folder = output_path
                signal = signal[0:int(lepow2(len(signal)))]
                tree = pywt.wavedec(signal, 'db5')
                gray()
                scalogram(tree)
                
                
                savefig(output_path_)
                close()
# Use the __init__ statement to run the commands when the module is imported
if __name__ == "__main__":
    generate_scaleograms(input_path='data/combined_wavs', output_path = 'data/scaleograms/human')
    #generate_scaleograms(input_path='data\\combined_wavsAI', output_path = 'data\\scaleograms\\ai')

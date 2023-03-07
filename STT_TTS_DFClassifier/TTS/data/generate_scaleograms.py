# Import libraries
import torch
import os
import pywt
import pytorch_wavelets
import scipy.io.wavfile
from scipy.signal import spectrogram, wavelets
import ptwt
import matplotlib.pyplot as plt
import numpy as np
import scaleogram as scg
import wave
import contextlib
use_cuda = torch.cuda.is_available()
device = torch.device("cuda" if use_cuda else "cpu")
# Define wavelet type and scales
wavelet = pywt.Wavelet('haar')
scales = np.arange(1, 512)

# Define input and output folders
input_folder_human = 'data\combined_wavs'
input_folder_ai = 'data\combined_wavsAI'
output_folder = 'data\scaleograms'
output_folder_human = os.path.join(output_folder, 'human')
output_folder_ai = os.path.join(output_folder, 'ai')

# Create output folders if they don't exist
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
if not os.path.exists(output_folder_human):
    os.mkdir(output_folder_human)
if not os.path.exists(output_folder_ai):
    os.mkdir(output_folder_ai)





# Loop through each wav file in each input folder
for folder in os.listdir(input_folder_human):
    Region_path = os.path.join(input_folder_human, folder)
    for file in os.listdir(Region_path):
        
        # Check if the file is a wav file
        if file.endswith('.wav'):
            # Read the wav file and get the sampling frequency and signal data
            sampling_frequency, signal = scipy.io.wavfile.read(os.path.join(Region_path, file))
            signal_torch = torch.from_numpy(signal.astype(np.float32))
            fname = os.path.join(Region_path, file)
            with contextlib.closing(wave.open(fname,'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
                print(f"duration:{duration}")
            t = np.arange(0,duration, 1 / sampling_frequency)
            print(f"sampling_frequency:{sampling_frequency}")
            # Perform continuous wavelet transform using pywt.cwt function
            print("performing cwt")
            signal_torch = signal_torch.to(device)
            
            
            cwtmatr, freqs = ptwt.dwt(signal_torch, scales, "haar", sampling_period=(1 /sampling_frequency))
            print("plotting scaleogram")
            fig, ax1 = plt.subplots(1,1, sharex = True, figsize = (10,8))
            im = ax1.pcolormesh(t,freqs, cwtmatr, vmin=0, cmap = "inferno" )  
            ax1.set_ylim(0,10)
            ax1.set_ylabel("Frequency in [Hz]")
            ax1.set_xlabel("Time in [s]")
            ax1.set_title(f"Scaleogram using wavelet MEXH")
            plt.tight_layout()
            plt.show()
            print("saving scaleogram to {output_folder}")
            if folder == input_folder_human:
                plt.savefig(os.path.join(output_folder_human, file.replace('.wav', '.png')))
            else:
                plt.savefig(os.path.join(output_folder_ai, file.replace('.wav', '.png')))
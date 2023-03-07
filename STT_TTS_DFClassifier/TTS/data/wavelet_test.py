
import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np
import torch
import os
import pywt
from pytorch_wavelets import DTCWTForward, DTCWTInverse
import scipy.io.wavfile
from scipy.signal import spectrogram, wavelets
import matplotlib.pyplot as plt
import numpy as np
import scaleogram as scg
import wave
import contextlib
"""
wavelet = 'morl'
scales = np.arange(1, 256)
sampling_frequency, signal = scipy.io.wavfile.read("data\combined_wavs\DR1C\FAKS0.wav")
coefficient, frequency =pywt.cwt(signal, scales, wavelet)

plt.imshow(coefficient, cmap='jet', aspect='auto')
plt.title("FAKS0 Human")
plt.xlabel('Time')
plt.ylabel('Scale')
plt.show

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
            

dwt_coeffs = ptwt.dwt(signal_torch, scales, "haar", sampling_period=(1 /sampling_frequency))
"""
from pylab import *
import pywt
import scipy.io.wavfile as wavfile
os.environ['KMP_DUPLICATE_LIB_OK']='True'

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

# Load the signal, take the first channel, limit length to a power of 2 for simplicity.




# Load the signal, take the first channel, limit length to a power of 2 for simplicity.
rate, signal = wavfile.read("data\TRAIN\DR1\FCJF0\SA1.WAV.wav")
output_folder = 'data\scaleograms'
signal = signal[0:int(lepow2(len(signal)))]
tree = pywt.wavedec(signal, 'db5')
output_folder_human = os.path.join(output_folder, 'human')
gray()
scalogram(tree)
show()
savefig('data\scaleograms\human\human.png')
"""
# Define input and output folders
input_folder_human = 'data\combined_wavs'
input_folder_ai = 'data\combined_wavsAI'
output_folder = 'data\scaleograms'
output_folder_human = os.path.join(output_folder, 'human')
output_folder_ai = os.path.join(output_folder, 'ai')
# Loop through each wav file in each input folder
for folder in os.listdir(input_folder_human):
    Region_path = os.path.join(input_folder_human, folder)
    for file in os.listdir(Region_path):
        
        # Check if the file is a wav file
        if file.endswith('.wav'):
            rate, signal = wavfile.read(os.path.join(Region_path, file))
            tree = pywt.wavedec(signal, 'db5')   
            # Plotting.
            gray()
            scalogram(tree, os.path.join(output_folder_human, file.replace('.wav', '.png')))
            show()
            
            """
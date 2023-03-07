# Import the necessary modules
import os
import torch
import pywt
import ptwt
import scaleogram as scg
import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import librosa
import math
torch.cuda.is_available()

# Define a function to extract .wav files from a given folder
def extract_wav(folder):
    # Initialize an empty list to store the file paths
    wav_files = []
    # Loop through the files in the folder
    for file in os.listdir(folder):
        # Check if the file is a .wav file and has a size of around 30 seconds (assuming 16 kHz sampling rate)
        if file.endswith(".wav"):
            # Append the file path to the list
            wav_files.append(os.path.join(folder, file))
    # Return the list of .wav files
    return wav_files

# Define a function to perform cuda accelerated cwt on a given .wav file using pywavelets
def cwt_cuda(wav_file):
    # Load the .wav file as an array using pywavelets (assuming mono channel)
    rate, data = wavfile.read(wav_file)
    t = librosa.get_duration(filename=wav_file)
    # Define the wavelet and scales parameters for cwt (you can change these according to your needs)
    wavelet = "cmor"
    scales = np.arange(1, 128)
    signal = torch.from_numpy(data)
    # Perform cwt using cuda backend (you need to install pycuda and skcuda for this)
    coeffs, freqs = ptwt.cwt(signal, scales, wavelet, sampling_period = 1/rate)

    cwt_matrix = coeffs.to("cpu")
    frequencies = freqs
    # Convert torch tensors to numpy arrays 
    cwt_matrix = cwt_matrix.numpy().astype(np.float)
    
    # Return the coefficients and frequencies arrays
    return cwt_matrix, frequencies, rate, t

# Define a function to create and save a scaleogram from a given cwt matrix using scaleogram
def save_scaleogram(coeffs, freqs, output_file, rate, t):
    # Create a figure object using scaleogram with default settings (you can change these according to your needs)
    # Show w.r.t. time and frequency
    fs = rate
    sampling_period = 1 / fs
    
    time = np.linspace(0 ,t, math.ceil(rate*t))
    plt.figure(figsize=(5, 2))
    plt.pcolor(time, freqs, coeffs)

    # Set yscale, ylim and labels
    plt.yscale('log')
    plt.ylim([1, 100])
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (sec)')
    plt.savefig('egg.png', dpi=150)
   
   # Close the figure object


# Define a main function that takes an input filepath and output filepath as arguments 
def main(input_filepath,output_filepath):
   # Loop through each of the subfolders in input_filepath named DR1C-DR8C 
   for i in range(1 ,9):
      subfolder = os.path.join(input_filepath,f"DR{i}C")
      # Extract all .wav files from each subfolder using extract_wav function 
      wav_files = extract_wav(subfolder) 
      # Loop through each .wav file in wav_files 
      for wav_file in wav_files: 
         # Perform cwt on each .wav file using cwt_cuda function 
         coeffs,freqs, rate, t = cwt_cuda(wav_file) 
         # Create an output filename based on input filename and output filepath 
         output_file = os.path.join(output_filepath,wav_file.split("/")[-1].replace(".wav",".png")) 
         # Create and save a scaleogram from each cwt matrix using save_scaleogram function 
         save_scaleogram(coeffs,freqs,output_file, rate, t)

# Call the main function with your desired input filepath and output filepath as arguments  
if __name__ == "__main__":
   main("data\combined_wavs","data\scaleograms\human")
main("data\combined_wavs","data\scaleograms\human")
# Import libraries
import os, sys, cv2, matplotlib.pyplot as plt, numpy as np, pandas as pd, pickle
import random
from random import seed, random, randint, sample

import tensorflow.keras as keras
from keras import backend as K
from keras.models import Model, load_model, Sequential
from keras.callbacks import ModelCheckpoint
from keras.layers import Input, Dense, GlobalMaxPool1D, Activation, MaxPool1D, Conv1D, Flatten, BatchNormalization
from keras.regularizers import l2
from keras.utils.vis_utils import plot_model
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2

import librosa 
import librosa.display
from sklearn.metrics import confusion_matrix, classification_report
from skimage.transform import resize
from scipy.signal import hilbert, chirp
from sklearn.preprocessing import MinMaxScaler
from librosa.filters import mel
import pywt
import scipy
from tqdm import tqdm
from sklearn.model_selection import StratifiedKFold

# Read a sample file
filename = os.getcwd() + "/data/raw/cv_delta/clips/common_voice_en_34925857.mp3"

# Read an audio file using librosa
y, sr = librosa.load(filename)

wavelet = 'morl' # wavelet type: morlet
sr = 8000 # sampling frequency: 8KHz
widths = np.arange(1, 64) # scales for morlet wavelet 
print("These are the scales that we are using: ", widths)
dt = 1/sr # timestep difference

frequencies = pywt.scale2frequency(wavelet, widths) / dt # Get frequencies corresponding to scales
print("These are the frequencies that re associated with the scales: ", frequencies)

# Compute continuous wavelet transform of the audio numpy array
wavelet_coeffs, freqs = pywt.cwt(y, widths, wavelet = wavelet, sampling_period=dt)
print("Shape of wavelet transform: ", wavelet_coeffs.shape)

# Display the scalogram. We will display a small part of scalogram because the length of scalogram is too big.
plt.imshow(wavelet_coeffs[:,:400], cmap='coolwarm')
plt.xlabel("Time")
plt.ylabel("Scales")
plt.yticks(widths[0::11])
plt.title("Scalogram")
plt.show()
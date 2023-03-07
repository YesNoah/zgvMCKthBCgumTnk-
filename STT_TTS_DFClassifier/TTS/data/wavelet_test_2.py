
# Import libraries
import os, sys, matplotlib.pyplot as plt, numpy as np, pandas as pd, pickle
import random
from random import seed, random, randint, sample

import scipy.io.wavfile as wavfile

import torch
from pytorch_wavelets import DTCWTForward, DTCWTInverse

rate, signal = wavfile.read("data\combined_wavs\DR1C\FAKS0.wav")
xfm = DTCWTForward(J=3, biort='near_sym_b', qshift='qshift_b').cuda()
X = torch.randn(10,5,64,64).cuda()
signal_torch = torch.from_numpy(signal).cuda()
print(signal_torch)
Yl, Yh = xfm(signal_torch)
ifm = DTCWTInverse(biort='near_sym_b', qshift='qshift_b').cuda()
Y = ifm((Yl, Yh))

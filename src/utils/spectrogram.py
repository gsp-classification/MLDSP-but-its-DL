
# *Import packages
import csv
import numpy as np
import pandas as pd
from scipy import signal as signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt
from PIL import Image

with open('../../data/processed/DNASignal.csv', mode='r') as csv_file:
    rows = csv.DictReader(csv_file)
    current_class = 'Birds'
    print("---------------------------------------------------------------------------------------------------------------")
    print("Creating spectrograms of class of "+current_class+".")
    for row in rows:
        if current_class != row['Class']:
            current_class = row['Class']
            print("Creating spectrograms of class of "+current_class+".")
        #print(row['Signal']
        classes = row['Class']
        sig = row['Signal']
        sig = sig[:-1]
        sig = sig[1:]
        sig = sig.split(', ')
        sig = list(map(int, sig))
        sig = np.array(sig)
        fs = 1
        ham = signal.get_window('hamming', 425)
        f, t, Sxx = signal.spectrogram(sig, fs, mode = 'magnitude')
        plt.pcolormesh(t, f, Sxx, shading='gouraud')
        plt.subplots_adjust(left=0,right=1,bottom=0,top=1)
        plt.axis('tight')
        plt.axis('off')
        plt.savefig('../../data/interim/spectrogram/'+classes+'/'+row['ID']+'.png', dpi=300)
        image = Image.open('../../data/interim/spectrogram/'+classes+'/'+row['ID']+'.png')
        img = image.convert('RGB')
        newsize = (224, 224) 
        im1 = img.resize(newsize)
        im1.save('../../data/processed/spectrogram/'+classes+'/'+row['ID']+'.png')


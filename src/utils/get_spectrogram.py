
# *Import packages
import csv
import os
from typing import final
import numpy as np
import pandas as pd
from scipy import signal as signal
import matplotlib.pyplot as plt
from PIL import Image
import multiprocessing
import concurrent.futures

def str_to_nparray(sig):
    sig1 = sig[:-1]
    sig2 = sig1[1:]
    sig3 = sig2.split(', ')
    sig4 = list(map(int, sig3))
    finsig = np.array(sig4)
    return finsig

def plot_spectrogram(array, out_path, fs = 1, window = 425, colour = 'gouraud'):
    ham = signal.get_window('hamming', window)
    f, t, Sxx = signal.spectrogram(array, fs, mode = 'magnitude')
    plt.pcolormesh(t, f, Sxx, shading = colour)
    plt.subplots_adjust(left=0,right=1,bottom=0,top=1)
    plt.axis('tight')
    plt.axis('off')
    plt.savefig(out_path, dpi=300)
    return out_path

def reshape_image(in_path, out_path):
    image = Image.open(in_path)
    img = image.convert('RGB')
    newsize = (224, 224) 
    im = img.resize(newsize)
    im.save(out_path)

def final_spectrogram(params):
    finsig, interim_out_path, processed_out_path = params[0], params[1], params[2]
    reshape_image(plot_spectrogram(finsig, interim_out_path), processed_out_path)
    print("working")

def main(path):
    with open(path, mode='r') as csv_file:
        rows = csv.DictReader(csv_file)
        current_class = 'Birds'
        print("---------------------------------------------------------------------------------------------------------------")
        print("Creating spectrograms of class of "+current_class+".")
        os.makedirs('../../data/interim/Vertebrates/'+current_class)
        os.makedirs('../../data/processed/Vertebrates/'+current_class)
        pool = multiprocessing.Pool()
        params =[]
        for row in rows:

            if current_class != row['Class']:
                current_class = row['Class']
                os.mkdir('../../data/interim/Vertebrates/'+current_class)
                os.mkdir('../../data/processed/Vertebrates/'+current_class)
                print("Creating spectrograms of class of "+current_class+".")
            
            sig = row['Signal']
            id = row['ID']
            finsig = str_to_nparray(sig)
            interim_out_path = '../../data/interim/Vertebrates/'+current_class+'/'+id+'.png'
            processed_out_path = '../../data/processed/Vertebrates/'+current_class+'/'+id+'.png'
            param = [finsig, interim_out_path, processed_out_path]
            params.append(param)

        #pool.starmap(final_spectrogram, params)
            #final_spectrogram(params)
        params = iter(params)
        #with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        #    executor.map(final_spectrogram, params)

if __name__ == "__main__":
    main(path = '../../data/processed/DNASignal.csv')
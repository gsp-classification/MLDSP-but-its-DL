
# *Import packages
import csv
import os
import shutil
import os.path
from typing import final
import numpy as np
import pandas as pd
from scipy import signal as signal
import matplotlib.pyplot as plt
from PIL import Image
#import multiprocessing
#import concurrent.futures

# *Function to change the input from the csv dataset into numpy array. Takes input string and outputs nparray.
def str_to_nparray(sig):
    sig1 = sig[:-1]
    sig2 = sig1[1:]
    sig3 = sig2.split(', ')
    sig4 = list(map(int, sig3))
    finsig = np.array(sig4)
    return finsig

# *Function to plot the spectrogram. Takes input array, string of output path (out_path), sampling frequency (fs), window size (window) 
# *and shading for the spectrograph(colour). Outputs the output path so that it can be nested with reshape_image()
def plot_spectrogram(array, out_path, fs = 1, window = 425, colour = 'gouraud'):
    ham = signal.get_window('hamming', window)
    f, t, Sxx = signal.spectrogram(array, fs, mode = 'magnitude')
    plt.pcolormesh(t, f, Sxx, shading = colour)
    plt.subplots_adjust(left=0,right=1,bottom=0,top=1)
    plt.axis('tight')
    plt.axis('off')
    plt.savefig(out_path, dpi=300)
    return out_path

# *Function to resize the spectrogram into a square. Takes input path of spectrogram image and output path of the resized image
def reshape_image(in_path, out_path):
    image = Image.open(in_path)
    img = image.convert('RGB')
    newsize = (224, 224) 
    im = img.resize(newsize)
    im.save(out_path)

# *Function to make the spectrogram from a list of parameters.
def final_spectrogram(params):
    sig, interim_out_path, processed_out_path = params[0], params[1], params[2]
    reshape_image(plot_spectrogram(str_to_nparray(sig), interim_out_path), processed_out_path)

# *Main function to loop over the iiles. Takes in input file path for DNASignal.csv
def main(path):

    # *Opening DNASignalcsv
    with open(path, mode='r') as csv_file:
        rows = csv.DictReader(csv_file)
        print("---------------------------------------------------------------------------------------------------------------")
        
        # *Removes the directories if made previously.
        if os.path.isdir('../../data/interim/Vertebrates'):
            shutil.rmtree('../../data/interim/Vertebrates')
        if os.path.isdir('../../data/processed/Vertebrates'):
            shutil.rmtree('../../data/processed/Vertebrates')
        #pool = multiprocessing.Pool()
        #params =[]
        i = True
        num = 1
        # *Looping over each genome in DNASignal.csv.
        for row in rows:

            # *For the first row
            if i:
                current_class = row['Class']
                i = False
                os.makedirs('../../data/interim/spectrograms/'+current_class)
                os.makedirs('../../data/processed/spectrograms/'+current_class)
                print("Creating spectrograms of class "+current_class+".")
            
            # *For subsequent rows
            if current_class != row['Class']:
                current_class = row['Class']
                os.mkdir('../../data/interim/spectrograms/'+current_class)
                os.mkdir('../../data/processed/spectrograms/'+current_class)
                print("Creating spectrograms of class "+current_class+".")
                num = 1
            
            # *Defining the parameters
            sig = row['Signal']
            id = row['ID']
            interim_out_path = '../../data/interim/spectrograms/'+current_class+'/'+id+'.png'
            processed_out_path = '../../data/processed/spectrograms/'+current_class+'/'+id+'.png'
            param = [sig, interim_out_path, processed_out_path]

            # *Calling the function
            final_spectrogram(param)
            
            #params.append(param)
            print('Number of IDs converted:', num)
            num = num + 1

        #pool.starmap(final_spectrogram, params)
            #final_spectrogram(params)
        #params = iter(params)
        #with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        #    executor.map(final_spectrogram, params)

if __name__ == "__main__":
    main(path = '../../data/processed/DNASignal.csv')
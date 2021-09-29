import numpy as np
from scipy import signal

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



class toSpectrogram():
    def __init__(self, signal, fs = 1, window = 425, color = 'gouraud'):
        self.signal = signal
        self.fs = fs
        self.window = window
        self.color = color

    def generateSpec(self):

        ham = signal.get_window('hamming', self.window)
        f, t, Sxx = signal.spectrogram(self.signal, self.fs, mode = 'magnitude')

        return t, f, Sxx

    def inNumpy(self):

        t, f, Sxx = self.generateSpec()
        fig = plt.figure(1)
        plt.pcolormesh(t, f, Sxx, shading = self.color)
        plt.subplots_adjust(left=0,right=1,bottom=0,top=1)
        plt.axis('tight')
        plt.axis('off')
        fig.canvas.draw()
        data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        plt.close(fig)
        return data

    def inPNG(self, path):

        t, f, Sxx = self.generateSpec()
        plt.pcolormesh(t, f, Sxx, shading = self.color)
        plt.subplots_adjust(left=0,right=1,bottom=0,top=1)
        plt.axis('tight')
        plt.axis('off')
        plt.savefig(path)


if __name__ == "__main__":
    spec = toSpectrogram()

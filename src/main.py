from utils.numericRep import toNumeric
import numpy as np
import matplotlib.pyplot as plt
from librosa import stft

seq = np.array('GTTAATGTAGCTTACATAAAGTGTGGCACTGAAAATGCTAAGACAGATTTTAAAATATCTCATAAACACACAGGTTTGGTCCTGACCTTGCTATTAATTTTTACTACGCTTACACATGCAAGTATCTGCATACCCGTGAAAATGCCCTTTACTACCCGTAAGTAGAACAGGAGCAGATATCAGGCACTTATAATGCCAAAGACATCTTGTTTAACCACACCCCTAAGGGAGCTCAGCAGTGATAAACATTGAATATAAGCGACACAAGCTTGAATCAGCGATAGTTAACAGAGTCGGTAAATCTCGTGCCAGCCACCGCGGTTATACGAGAGACTCAAATTAATATAATCGGCCCAAAGAGTGGTTAGGAGCGTAAATCAAATAGGGTTAAAAACTAACCCCGCTGTCGTACGCAGAGGTTAAAAAAAGCACAACACCGAAAGTAACCCTATAAAAACACCACTGAACCCACGACAGCTAGGACACAAACTGGGATTAGATACCCCACTATGCCTAGCCATAA')

X = toNumeric(seq).PP()

fs = 50          # assumed sample frequency in Hz
window_size = 10  # 2048-sample fourier windows
stride = 2        # 512 samples between windows
wps = fs/float(2) # ~86 windows/second
Xs = np.empty([int(2*wps),10])

X_libs = stft(X, n_fft=window_size, hop_length=stride)
X_libs = np.abs(X_libs)[:,:int(2*wps)]

fig = plt.figure(figsize=(20,7))
plt.imshow(X_libs[0:150],aspect='auto')
plt.gca().invert_yaxis()
fig.axes[0].set_xlabel('windows (~86Hz)')
fig.axes[0].set_ylabel('frequency')
plt.show()
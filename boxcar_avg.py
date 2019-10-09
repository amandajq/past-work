import numpy as np
import matplotlib.pyplot as plt
from sys import argv
from astropy.convolution import convolve, Box1DKernel

#takes user input for file name
basename = argv[1]

#reads in file header and stores wavelength values
f=open(basename,'r')
f.readline()
wlen=f.readline()
f.close()

#reads in file data, skipping header
dat = np.genfromtxt(basename,skip_header=2,skip_footer=1,delimiter=',')
#stores time and intensity values
time = dat[:,0]
inten = dat[:,1:]

#formats wavelength data
wlen = np.array([float(i) for i in wlen.split(',')[1:]])

#creates an array of data for each frame and takes the means
list = []
for i,flux in enumerate(inten):
	a = flux
	list.append(a)
arr = np.array(list)
means = arr.mean(axis=0)

#creates a 4x4 boxcar average of the intensity means
smoothed_signal = convolve(means,Box1DKernel(4))
stdev = np.std(smoothed_signal, dtype=np.float64)

#creates plot for the boxcar averaged data
plt.xlabel("Wavelength")
plt.ylabel("Mean Intensity")
plt.title('9/05/19 Jupiter Data 4x4 Boxcar Average')
plt.plot(wlen,smoothed_signal,label='4x4 Boxcar Average Data',color='r')
#plots the regular data for comparison
plt.plot(wlen,means,alpha=.4,label='Regular Mean Data',color='b')
plt.legend(loc='upper left')

plt.show()
import numpy as np
import matplotlib.pyplot as plt
from sys import argv

basename = argv[1]
f=open(basename,'r')
f.readline()
wlen=f.readline()
f.close()

dat = np.genfromtxt(basename,skip_header=2,skip_footer=1,delimiter=',')
wlen = np.array([float(i) for i in wlen.split(',')[1:]])
inten = dat[70,1:]

plt.title("Plot of one spectrum of Jupiter")
plt.xlabel("wavelength (nm)")
plt.ylabel("Intensity (counts)")
plt.plot(wlen,inten, alpha=.7, color='r')
plt.show()
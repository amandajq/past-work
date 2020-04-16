import numpy as np
import matplotlib.pyplot as plt
from sys import argv

basename = argv[1]
base_dark = argv[2]
base_flat = argv[3]
f=open(basename,'r')
f.readline()
wlen=f.readline()
f.close()

f_dark=open(base_dark,'r')
f_dark.readline()
wlen_dark=f_dark.readline()
f_dark.close()

f_flat=open(base_flat,'r')
f_flat.readline()
wlen_flat=f_flat.readline()
f_flat.close()

dat = np.genfromtxt(basename,skip_header=2,skip_footer=1,delimiter=',')
time = dat[:,0]
inten = dat[:,1:]

dat_dark = np.genfromtxt(base_dark,skip_header=2,skip_footer=1,delimiter=',')
time_dark = dat_dark[:,0]
inten_dark = dat_dark[:,1:]

dat_flat = np.genfromtxt(base_flat,skip_header=2,skip_footer=1,delimiter=',')
time_flat = dat_flat[:,0]
inten_flat = dat_flat[:,1:]

wlen = np.array([float(i) for i in wlen.split(',')[1:]])
list = []
for i,flux in enumerate(inten):
	a = flux
	list.append(a)
	arr = np.array(list)
means = arr.mean(axis=0)

wlen_dark = np.array([float(d) for d in wlen_dark.split(',')[1:]])
list_dark = []
for j,flux_dark in enumerate(inten_dark):
	a_dark = flux_dark
	list_dark.append(a_dark)
	arr_dark = np.array(list_dark)
means_dark = arr_dark.mean(axis=0)

wlen_flat = np.array([float(q) for q in wlen_flat.split(',')[1:]])
list_flat = []
for k,flux_flat in enumerate(inten_flat):
	a_flat = flux_flat
	list_flat.append(a_flat)
	arr_flat = np.array(list_flat)
means_flat = arr_flat.mean(axis=0)

subtracted = means-means_dark
final_data = subtracted-means_flat

plt.title("Venus intensity means 11/04/19")
plt.xlabel("wavelength (nm)")
plt.ylabel("Intensity means (counts)")
#print(wlen.shape)
#print(wlen_dark.shape)
#print(means.shape)
#print(means_dark.shape)
plt.plot(wlen_dark,means_dark,alpha=.7,color='r',label='Intensity from detector')
plt.plot(wlen_flat,means_flat,color='g',label='Intensity from clear sky')
#plt.plot(wlen,final_data,label='Intensity from Venus, flat and dark subtracted')
#plt.plot(wlen,means,label='Raw Intensity from Venus')
plt.legend(loc='upper left')
plt.plot()
plt.show()
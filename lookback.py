import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt


def E(z):
	return (.28*(1+z)**3+.72)**(.5)


def func(z):
	return (1./((1+z)*E(z)))

tH = 13.6

zs = np.linspace(0,20,100)
tL = []

for z in zs:
   tL.append(tH*quad(func,0,z)[0])

plt.plot(zs,tL)
plt.xlabel('Z (Redshift)')
plt.ylabel('Lookback time in Gyr')

plt.savefig('lookback.png')
plt.show()
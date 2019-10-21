import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt('veldispersion.txt')

R = data[:,0]
sigma = data[:,1]

R =  8500*np.pi*R/60/180 # pc
G = 4.5e-3
Mass = R * sigma**2 / G 

plt.plot(R,Mass)
plt.ylabel("Enclosed Mass in ($M_{\odot}$)")
plt.xlabel("Radius in pc")
plt.title("Enclosed Mass at Center of Milky Way")
plt.savefig('veldispersion.png')
plt.show()
plt.close()
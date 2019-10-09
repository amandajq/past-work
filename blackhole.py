import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt('bhdata.txt')
x = data[:,0]
y = data[:,1]
logx = np.log10(x)
logy = np.log10(y)
linear_fit = np.polyfit(logx,logy,1)
logy_fit = linear_fit[0]*logx+linear_fit[1]
numerator = (logy-logy_fit)**2
chi2 = sum(numerator)
print(type(chi2))
plt.text(2, 10, '$\chi^2$ = %.2f' %(chi2) )
plt.text(2, 9.5, '$\log\,M_{\mathrm{BH}} = %.1f\,\log\,\sigma_V - %.1f$' %(linear_fit[0], np.sign(linear_fit[1])*linear_fit[1]) )
plt.scatter(logx,logy)
plt.plot(logx,logy_fit)
plt.ylabel("galaxy velocity dispersion (sigma) km/s")
plt.xlabel("black hole mass in solar masses")
plt.title("Black-Hole Sigma Relation")
plt.savefig('blackhole-sigma.png')
plt.show()

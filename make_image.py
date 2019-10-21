from astropy.io import fits
from scipy.ndimage.interpolation import shift
import numpy as np


def subtract_overscan(filename):
	image = fits.getdata(filename)
	overscan = np.mean(image[:,2048:])
	return image[:,:2048]-overscan

m42_image_93 = subtract_overscan('2018_04_11_oclass_0093.fits')
m42_image_94 = subtract_overscan('2018_04_11_oclass_0094.fits')
m42_image_95 = subtract_overscan('2018_04_11_oclass_0095.fits')
m95_image_97 = subtract_overscan('2018_04_11_oclass_0097.fits')
m95_image_98 = subtract_overscan('2018_04_11_oclass_0098.fits')
m95_image_99 = subtract_overscan('2018_04_11_oclass_0099.fits')
m95_image_100 = subtract_overscan('2018_04_11_oclass_0100.fits')
m95_image_101 = subtract_overscan('2018_04_11_oclass_0101.fits')
m95_image_102 = subtract_overscan('2018_04_11_oclass_0102.fits')
m95_image_103 = subtract_overscan('2018_04_11_oclass_0103.fits')
m95_image_104 = subtract_overscan('2018_04_11_oclass_0104.fits')
m95_image_105 = subtract_overscan('2018_04_11_oclass_0105.fits')
m95_image_106 = subtract_overscan('2018_04_11_oclass_0106.fits')

flatU = subtract_overscan('Uflat.fits')
flatB = subtract_overscan('Bflat.fits')
flatV = subtract_overscan('Vflat.fits')
flatR = subtract_overscan('Rflat.fits')


m42_image_93 = m42_image_93/flatV
m42_image_94 = m42_image_94/flatV
m42_image_95 = m42_image_95/flatU
m95_image_97 = m95_image_97/flatU
m95_image_98 = m95_image_98/flatU
m95_image_99 = m95_image_99/flatB
m95_image_100 = m95_image_100/flatB
m95_image_101 = m95_image_101/flatV
m95_image_102 = m95_image_102/flatV
m95_image_103 = m95_image_103/flatR
m95_image_104 = m95_image_104/flatR
m95_image_105 = m95_image_105/flatR
m95_image_106 = m95_image_106/flatR


shift_94 = shift(m42_image_94,(2,6))
fits.writeto('94_shift.fits',shift_94,overwrite=True)
fits.writeto('93_image.fits',m42_image_93,overwrite=True)


V_median_m42 = np.median([shift_94,m42_image_93],axis=0)
fits.writeto('m42_v.fits',V_median_m42,overwrite=True)

shift_95 = shift(m42_image_95,(4,11))
fits.writeto('95_shift.fits',shift_95,overwrite=True)
fits.writeto('m42_u.fits',shift_95,overwrite=True)

v_u_avg = np.mean([V_median_m42,shift_95],axis=0)
fits.writeto('m42_v_u_avg.fits',v_u_avg,overwrite=True)

#######
#thing = np.mean(v-make r, u-make blue, avg-make green)

m95_shift_98 = shift(m95_image_98,(-5,0))
fits.writeto('98_shift.fits',m95_shift_98,overwrite=True)

U_median_m95 = np.median([m95_image_97,m95_shift_98],axis=0)
fits.writeto('m95_u.fits',U_median_m95,overwrite=True)



shift_99 = shift(m95_image_99,(-8,40))
fits.writeto('99_shift.fits',shift_99,overwrite=True)

shift_100 = shift(m95_image_100,(-10,48))
fits.writeto('100_shift.fits',shift_100,overwrite=True)

B_median_m95 = np.median([shift_100,shift_99],axis=0)
fits.writeto('m95_b.fits',B_median_m95,overwrite=True)

###############################################

shift_101 = shift(m95_image_101,(-14,51))
fits.writeto('101_shift.fits',shift_101,overwrite=True)

shift_102 = shift(m95_image_102,(-16,54))
fits.writeto('102_shift.fits',shift_102,overwrite=True)

V_median_m95 = np.median([shift_101,shift_102],axis=0)
fits.writeto('m95_v.fits',V_median_m95,overwrite=True)

####################################

shift_103 = shift(m95_image_103,(-17,59))
fits.writeto('103_shift.fits',shift_103,overwrite=True)

shift_104 = shift(m95_image_104,(-18,62))
fits.writeto('104_shift.fits',shift_104,overwrite=True)

shift_105 = shift(m95_image_105,(-21,66))
fits.writeto('105_shift.fits',shift_105,overwrite=True)

shift_106 = shift(m95_image_106,(-24,20))
fits.writeto('106_shift.fits',shift_106,overwrite=True)

R_median_m95 = np.median([shift_103,shift_104,shift_105,shift_106],axis=0)
fits.writeto('m95_r.fits',R_median_m95,overwrite=True)
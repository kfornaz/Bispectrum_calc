import numpy as np
import healpy as hp
import ConfigParser
from astropy.io import fits as pyfits
import matplotlib.pyplot as plt
import sys

#21cm from Flask
#decrescente
#mapas_21 = np.zeros((30,786432))
#for i in range(1,30):
#    a=30-i
#    mapas_21[a,:]= hp.read_map('delta-f1z' + str(i) + '.fits')
#    print "lendo-->", a


#crescente
mask_maps = np.zeros((30,786432))
for i in range(1,30):
    a=i-1
    mask_maps[a,:]= hp.read_map('/home/karin/Desktop/gnilc/Cubo_Flask_crescente/Redshifts_bins/Foregrounds_Redshift/fits/Mask_Foregrounds_Cubo_Redshift_' + str(i) + '.fits')
    print "lendo-->", a

pyfits.writeto('Mask_Foregrounds_Cubo_Redshift_21_total', mask_maps)
print "salvei pyfits 21"
hp.mollview(mask_maps[0,:])

print "salvei flask maps"

# Foregrounds Maps

mapas_foreground = pyfits.getdata("foreground_cube_Nside256.fits")
print (mapas_foreground[0,:])
mapas_final = mapas_foreground*mask_maps
pyfits.writeto('cube_finalmap_delta_foregrounds_mask.fits', mapas_final)
hp.mollview(mapas_final[0,:])
data = pyfits.getdata("cube_finalmap_delta_foregrounds_mask.fits")
plt.show()


# encoding: utf-8
##############################################################################
##  algorithm for summing up two different outputs maps                 #####
##  Flask                                                 
##                                                                       #####
##  Foregrounds 
## Authors: Karin Fornazier
## Email: karin.fornazier@gmail.com
## Supervisor: F.B. Abdalla
## Latest Version June 2019
###########################################################################
###########################################################################

import numpy as np
import healpy as hp
import ConfigParser
from astropy.io import fits as pyfits
import matplotlib.pyplot as plt
import sys

#21cm from Flask
#decrescente



#crescente
#mapas_21 = np.zeros((30,786432))
#for i in range(1,31):
#    a=i-1
#    mapas_21[a,:]= hp.read_map('delta-f1z' + str(i) + '.fits')
#    print "lendo-->", a

pyfits.writeto('delta_flask_21_cube_decrescente.fits', mapas_21)
print "salvei pyfits 21"
hp.mollview(mapas_21[0,:])

print "salvei flask maps"

# Foregrounds Maps

mapas_foreground = pyfits.getdata("foreground_cube_Nside256.fits")
print (mapas_foreground[0,:])
mapas_final = mapas_foreground + mapas_21
pyfits.writeto('cube_finalmap_delta_foregrounds_256.fits', mapas_final)
hp.mollview(mapas_final[0,:])
#data = pyfits.getdata("cube_finalmap_delta_foregrounds.fits")
plt.show()


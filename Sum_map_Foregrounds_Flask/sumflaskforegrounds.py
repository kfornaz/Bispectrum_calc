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
mapas_21 = np.zeros((30,786432))
for i in range(1,30):
    a=30-i
    mapas_21[a,:]= hp.read_map('counts-f1z' + str(i) + '.fits')
    print "lendo-->", a

#pyfits.writeto('counts_flask_testepyfits.fits', mapas_21)
#print "salvei pyfits 21"
hp.write_map('counts_flask_somado.fits', mapas_21)
hp.mollview(mapas_21[0,:])

print "salvei flask maps"

# Foregrounds Maps

mapas_foreground = pyfits.getdata("foreground_cube_flask_redshift_256.fits")

mapas_final = mapas_foreground + mapas_21
hp.write_map('mapas_soma_flask_foregrounds.fits', mapas_final)
hp.mollview(mapas_final[0,:])
data = pyfits.getdata("mapas_soma_flask_foregrounds.fits")
plt.show()

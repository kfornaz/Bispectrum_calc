# encoding: utf-8
##############################################################################
## Algorithm for creating a Cube FG Rotated, Smoothed and 
# Temperature Changed 
##                                                                       #####
## ## Authors: Karin Fornazier, Alessando Marins Filipe Abdala
## Email: karin.fornazier@gmail.com
## Supervisor: F.B. Abdalla
## Latest Version August 2019
###########################################################################
###########################################################################
import healpy as hp
import numpy as np
from astropy.io import fits as pyfits
import matplotlib.pyplot as plt
plt.switch_backend('agg')

#Loop for all redshift bins
FG_maps_Rotated_Smooth_Temp = np.zeros((30,786432))
for i in range(0,30):
    a=i
    FG_maps_Rotated_Smooth_Temp[a,:]= pyfits.getdata('FG_256_Rotate_Celestial_Galactic_Smooth_Temp_Redshift_' + str(i) + '.fits')
    print "lendo-->", a    

pyfits.writeto('FG_maps_Rotated_Smooth_Temp_Cube_256.fits', FG_maps_Rotated_Smooth_Temp)
print "salvei pyfits cubo"

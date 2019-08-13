# encoding: utf-8
##############################################################################
## Algorithm for creating a Cube 21cm                                    #####
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
Flask_21_maps_Smooth = np.zeros((30,786432))
for i in range(0,30):
    a=i
    Flask_21_maps_Smooth[a,:]= pyfits.getdata('21_Flask_256__Smooth_decres_' + str(i) + '.fits')
    print "lendo-->", a
    

pyfits.writeto('Flask_21cm_Smooth_Cube_256.fits', Flask_21_maps_Smooth)
print "salvei pyfits cubo"



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
plt.switch_backend('agg')
import sys

#21cm from Flask
mapas_21 = pyfits.getdata("Flask_21cm_Smooth_Cube_256.fits")

# Foregrounds Maps

mapas_foreground = pyfits.getdata("FG_maps_Rotated_Smooth_Temp_Cube_256.fits")
print (mapas_foreground[0,:])


mapas_final = mapas_foreground + mapas_21
pyfits.writeto('Cube_21_FG_maps_Rotated_Smooth_Temp_256.fits', mapas_final)



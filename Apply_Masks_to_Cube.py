import numpy as np
import healpy as hp# encoding: utf-8
##############################################################################
## Algorithm for reading cube of maps and separate then in diferent      #####
## bins of redshift applying a acceptance masks (BINGO one)              #####
## 
##
## Authors: Karin Fornazier,Filipe Abdala
## Email: karin.fornazier@gmail.com
## Supervisor: F.B. Abdalla
## Latest Version August 2019
###########################################################################
###########################################################################
import numpy as np
import healpy as hp
import ConfigParser
from astropy.io import fits as pyfits
import matplotlib.pyplot as plt
import sys

mask_maps = pyfits.getdata("Mask_Total.fits")

print "li mask"

# Foregrounds Maps -> applying mask to a fits map

mapas_foreground = pyfits.getdata("Cube_21_FG_maps_Rotated_Smooth_Temp_256.fits")
print "li cubo"

mapas_final = mapas_foreground*mask_maps

pyfits.writeto('Cube_Final_21_FG_Modified_Mask.fits', mapas_final)


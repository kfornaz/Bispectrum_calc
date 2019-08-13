# encoding: utf-8
##############################################################################
## Script for Rotating, Smoothing and Tempretature Subtration in loop
# over 30 maps 
##                                                                       #####
## ## Authors: Karin Fornazier, Alessando Marins and Filipe Abdala
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


def map_rotation(m = None, coord_in = "C", coord_out = "G"):
   
# Basic HEALPix parameters
   coord = [coord_in,coord_out]
   npix  = m.shape[-1]
   nside = hp.npix2nside(npix)
   ang   = hp.pix2ang(nside, np.arange(npix))  
 # Select the coordinate transformation
   rot = hp.Rotator(coord=reversed(coord))

   # Convert the coordinates
   ang = rot(*ang)
   pix = hp.ang2pix(nside, *ang)

   return m[..., pix]

FWHM = np.radians(0.0116355)
SIGMA = np.radians(5)
T_FG_max  = 3e5
    
FG= pyfits.getdata("foreground_cube_Nside256.fits")
for i in range(0,30):
    a=i
    hp.mollview(FG[a,:],title="Foregrounds Nside256 Redshift="+ str(i))
    plt.savefig('Foregrounds/FG_256_Redshift_'+ str(i) + '.png')
    pyfits.writeto('Foregrounds/FG_256_Redshift_'+str(i)+ '.fits', FG[a,:]) 
        
    #Apply rotation
    FGr= map_rotation(FG[a,:]) 
    hp.mollview(FGr,title="Foregrounds Nside256 Rotate C--> G Redshift ="+ str(i))
    print "lendo Foregrounds -->", a
    plt.savefig('Foregrounds_Rotate/FG_256_Rotate_Celestial_Galactic_Redshift_'+ str(i) + '.png')
    pyfits.writeto('Foregrounds_Rotate/FG_256_Rotate_Celestial_Galactic_Redshift_'+str(i)+ '.fits', FGr) 
    
    #Apply Smooth
    FGrsm = hp.sphtfunc.smoothing(FGr,fwhm=0.0116355)
    hp.mollview(FGrsm,title="FG Nside256 Rotate C--> G Smooth Redshift "+ str(i))
    print "lendo Foregrounds Rotate-->", a
    plt.savefig('Foregrounds_Rotate_Smooth/FG_256_Rotate_Celestial_Galactic_Smooth_Redshift_'+ str(i) + '.png')
    pyfits.writeto('Foregrounds_Rotate_Smooth/FG_256_Rotate_Celestial_Galactic_Smooth_Redshift_'+str(i)+ '.fits', FGrsm) 
    
    #Apply Temperature > T0
    FGrsm[ FGrsm > T_FG_max ] = 0
    hp.mollview(FGrsm,title="FG Nside256 Rotate C--> G Smooth and T> 3e5 Redshift ="+ str(i))
    print "lendo Foregrounds Rotate Smooth-->", a
    plt.savefig('Foregrounds_Rotate_Smooth_Temperature/FG_256_Rotate_Celestial_Galactic_Smooth_Temp_Redshift_'+ str(i) + '.png')
    pyfits.writeto('Foregrounds_Rotate_Smooth_Temperature/FG_256_Rotate_Celestial_Galactic_Smooth_Temp_Redshift'+str(i)+ '.fits', FGrsm)  
    
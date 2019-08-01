import os,sys
import numpy as np
import healpy as hp
from math import *
from astropy.io import ascii, fits
#from astropy.table import Table, join, hstack, vstack

NSIDE      = 256 
phi_mask   = True
theta_mask = False
phi_min    = -22.5
phi_max    = -2.5
theta_min  = -90
theta_max  = 90   

start = 1
end = 30    
for i in range(start, end):
    #matrixf = np.loadtxt("B_ell_ell_delta_flask_21_cube256_redshift_"+str(i)+ ".txt", delimiter=',')
    NPIXa  = fits.getdata("/home/karin/Desktop/gnilc/Cubo_Flask_crescente/Redshifts_bins/Foregrounds_Redshift/fits/Foregrounds_Cubo_Redshift_"+str(i)+ ".fits", delimiter=',')
    NPIX       = hp.nside2npix(NSIDE)
    bingo_mask = np.zeros((NPIX), dtype=bool)
    #bingo_mask = np.ones((NPIX))
    
    for pixel in range(NPIX):
        theta,phi = hp.pix2ang(NSIDE,pixel, lonlat=True, nest=False)
        if (phi>phi_min)*(phi<phi_max)*phi_mask and not theta_mask:
            bingo_mask[pixel] = NPIXa[NPIX]
        elif (theta>theta_min)*(theta<theta_max)*theta_mask and not phi_mask:
            bingo_mask[pixel] = NPIXa[NPIX]
        elif (theta>theta_min)*(theta<theta_max)*theta_mask*(phi>phi_min)*(phi<phi_max)*phi_mask:
            bingo_mask[pixel] = NPIXa[NPIX]
        else:
            pass
    
    print "lendo--> Redshift", i
    hp.write_map('/home/karin/Desktop/gnilc/Cubo_Flask_crescente/Redshifts_bins/Foregrounds_Redshift/fits/MaskA_Foregrounds_Cubo_Redshift_'+str(i)+ '.fits', bingo_mask)

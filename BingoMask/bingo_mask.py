import os,sys
import numpy as np
import healpy as hp
from math import *
from astropy.io import ascii, fits
from astropy.table import Table, join, hstack, vstack



def maskdir(name="BINGO_MASK"):
    path = os.getcwd()
    path_maskdir = os.path.join(path,name)
    if not os.path.isdir(path_maskdir):
        os.mkdir(path_maskdir)
    else: pass

NPIXa  = fits.getdata("foreground_cube__bispectrumforegrounds_bingo_mask.fits")
NPIX = hp.get_map_size(NPIXa[1])
NSIDE = hp.npix2nside(NPIX)
#NSIDE      = 1024
theta_mask = False
phi_mask   = True
phi_min    = -52.5
phi_max    = -11.5
theta_min  = 0
theta_max  = 0 


NPIX       = hp.nside2npix(NSIDE)
bingo_mask = np.zeros((NPIX), dtype=bool)

for pixel in range(NPIX):
    theta,phi = hp.pix2ang(NSIDE,pixel, lonlat=True)
    
    if (phi>phi_min)*(phi<phi_max)*phi_mask and not theta_mask:
        bingo_mask[pixel] = True
    elif (theta>theta_min)*(theta<theta_max)*theta_mask and not phi_mask:
        bingo_mask[pixel] = True
    elif (theta>theta_min)*(theta<theta_max)*theta_mask*(phi>phi_min)*(phi<phi_max)*phi_mask:
        bingo_mask[pixel] = True
    else:
        pass

if phi_mask and not theta_mask:
    file = "_".join(("BingoMask",str(NSIDE),"phi",str(phi_min),str(phi_max)))
elif theta_mask and not phi_mask:
    file = "_".join(("BingoMask",str(NSIDE),"theta",str(theta_min),str(theta_max)))
elif theta_mask*phi_mask:
    file = "_".join(("BingoMask",str(NSIDE),"phi",str(phi_min),str(phi_max),"theta",str(theta_min),str(theta_max)))
else:
    file = "_".join(("BingoMask",str(NSIDE),"no_mask"))

file = ".".join((file,"fits"))
path = os.getcwd()
path = os.path.join(path,"BINGO_MASK")
path = os.path.join(path,file)
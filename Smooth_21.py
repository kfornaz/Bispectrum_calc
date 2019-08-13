# encoding: utf-8
##############################################################################
## Algorithm for Applying Smooth condition to 21 cm maps                 #####
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

#Value for FWHM em radians - Bingo case 40 arc min
FWHM = np.radians(0.0116355)
    
Flask_21= pyfits.getdata("Cubo_delta_Flask_21_256_decrescente.fits")
for i in range(0,30):
    a=i
    F_21=Flask_21[a,:]
    hp.mollview(F_21,title="Delta Flask 21 Nside256 Redshift="+ str(i))
    plt.savefig('Smooth_Maps/21_Flask_256_decres'+ str(i) + '.png')
    pyfits.writeto('Smooth_Maps/21_Flask_256_decres'+str(i)+ '.fits', F_21) 
        
    #Apply Smooth
    Flask_21_Smooth = hp.sphtfunc.smoothing(F_21,fwhm=0.0116355)
    hp.mollview(Flask_21_Smooth,title="Delta Flask 21 Nside256 Smooth Redshift= "+ str(i))
    print "lendo 21_Flask_256_-->", a
    plt.savefig('Smooth_Maps/21_Flask_256__Smooth_decres_'+ str(i) + '.png')
    pyfits.writeto('Smooth_Maps/21_Flask_256__Smooth_decres_'+str(i)+ '.fits', Flask_21_Smooth) 
    
       
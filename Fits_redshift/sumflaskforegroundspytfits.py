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
#mapas_21 = np.zeros((30,786432))
#for i in range(1,30):
#    a=30-i
#    mapas_21[a,:]= hp.read_map('delta-f1z' + str(i) + '.fits')
#    print "lendo-->", a


#crescente
mapas_21 = np.zeros((30,786432))
for i in range(1,30):
    a=i
    mapas_21[a,:]= hp.read_map('delta-f1z' + str(i) + '.fits')
    print "lendo-->", a



pyfits.writeto('delta_flask_21_matrixmap_tognilc_crescente.fits', mapas_21)
print "salvei pyfits 21"
#hp.write_map('counts_flask_teste.fits', mapas_21)
hp.mollview(mapas_21[0,:])

print "salvei flask maps"

# Foregrounds Maps

mapas_foreground = pyfits.getdata("foreground_cube_Nside256.fits")

mapas_final = mapas_foreground + mapas_21
pyfits.writeto('final_map_delta_foregroundscrescente.fits', mapas_final)
#hp.write_map('mapas_final0.fits', mapas_final)
hp.mollview(mapas_final[0,:])
data = pyfits.getdata("final_map_delta_foregroundscrescente.fits")
plt.show()

# Synch
#mapas_synch = pyfits.getdata("synch_cube_newtext256.fits")

#mapas_final_synch = mapas_synch + mapas_21
#pyfits.writeto('final_map_delta_synch.fits', mapas_final_synch)
#hp.write_map('mapas_final0.fits', mapas_final)
#hp.mollview(mapas_final_synch[0,:])
#data = pyfits.getdata("final_map_delta_synch.fits")
#plt.show()

# ame
#mapas_ame = pyfits.getdata("ame_cube_newtext256.fits")

#mapas_final_ame = mapas_ame + mapas_21
#pyfits.writeto('final_map_delta_ame.fits', mapas_final_ame)
#hp.write_map('mapas_final0.fits', mapas_final)
#hp.mollview(mapas_final_ame[0,:])
#data = pyfits.getdata("final_map_delta_ame.fits")
#plt.show()

# free free
#mapas_free = pyfits.getdata("ame_cube_newtext256.fits")

#mapas_final_free = mapas_free + mapas_21
#pyfits.writeto('final_map_delta_free.fits', mapas_final_free)
#hp.write_map('mapas_final0.fits', mapas_final)
#hp.mollview(mapas_final_free[0,:])
#data = pyfits.getdata("final_map_delta_free.fits")
#plt.show()

#CMB cmb_cube_newtext256.fits   

#mapas_cmb = pyfits.getdata("cmb_cube_newtext256.fits")

#mapas_final_cmb = mapas_cmb + mapas_21
#pyfits.writeto('final_map_delta_cmb.fits', mapas_final_cmb)
#hp.write_map('mapas_final0.fits', mapas_final)
#hp.mollview(mapas_final_free[0,:])
#data = pyfits.getdata("final_map_delta_cmb.fits")
#plt.show()

#thermal cmb_cube_newtext256.fits   

#mapas_thermal = pyfits.getdata("thermal_dust_cube_newtext256.fits")

#mapas_final_thermal = mapas_thermal + mapas_21
#pyfits.writeto('final_map_delta_thermal.fits', mapas_final_thermal)
#hp.write_map('mapas_final0.fits', mapas_final)
#hp.mollview(mapas_final_free[0,:])
#data = pyfits.getdata("final_map_delta_thermal.fits")
#plt.show()

#point sources point_sources_cube_newtext256.fits  

#mapas_point = pyfits.getdata("point_sources_cube_newtext256.fits")

#mapas_final_point = mapas_point + mapas_21
#pyfits.writeto('final_map_delta_point.fits', mapas_final_point)
#hp.write_map('mapas_final0.fits', mapas_final)
#hp.mollview(mapas_final_free[0,:])
#data = pyfits.getdata("final_map_delta_point.fits")
#plt.show()

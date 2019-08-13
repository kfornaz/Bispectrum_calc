# encoding: utf-8

##############################################################################
## Algorithm for save each redshift bin in a fits file                  #####
##                                                                      #####
## Authors: Karin Fornazier, Filipe Abdalla
## Email: karin.fornazier@gmail.com
## Supervisor: F.B. Abdalla
## Latest Version July 2019
###########################################################################
###########################################################################


from astropy.io import fits as pyfits
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt

for i in range(0,30):
    a=i
    mapas_21= pyfits.getdata('Cube_flask_21_Smooth_mask2.fits')
    print "lendo Flask-->", a
    hp.mollview(mapas_21[a,:],title = "21cm Masked Nside 256 Redshift = "+ str(i))
    #plt.show()
    plt.savefig('21cm_N256_Redshift_Masked_'+ str(i) + '.png')
    pyfits.writeto('21cm_N256_Redshift_Masked_'+str(i)+ '.fits',mapas_21[a,:])


map_total = pyfits.getdata('Cube_Final_21_FG_Modified_mask.fits')
for i in range(0,30):
    a=i-1
    hp.mollview(map_total[a,:],title="Nside 256 Foregrounds + 21 cm  Modified Redshift ="+ str(i))
    #plt.show()
    print "lendo Cubo Total-->", a
    plt.savefig('Cube_N256_Foregrounds_Mod_mask_Redshift_'+ str(i) + '.png')
    pyfits.writeto('Cube_N256_Foregrounds_Mod_mask_Redshift_'+str(i)+ '.fits',map_total[a,:])


#foregrounds = pyfits.getdata('/share/karin/Desktop/gnilc/Cubo_Flask_crescente/foreground_cube_Nside256.fits')
#for i in range(1,31):
#    a=i-1
#    hp.mollview(foregrounds[a,:],title="Foregrounds Cube Redshift_"+ str(i))
#    #plt.show()
#    print "lendo Foregrounds-->", a
#    plt.savefig('/home/karin/Desktop/gnilc/Cubo_Flask_crescente/Redshifts_bins/Foregrounds_Redshift/Foregrounds_Cubo_Redshift_'+ str(i) + '.png')
#    pyfits.writeto('/home/karin/Desktop/gnilc/Cubo_Flask_crescente/Redshifts_bins/Foregrounds_Redshift/Foregrounds_Cubo_Redshift_'+str(i)+ '.fits', foregrounds[a,:])

#cubo_reconstructed = pyfits.getdata('/share/data1/kfornazier/Analises/reconstructed_maps_bingomaskpriorflask2048.fits')
#for i in range(1,31):
#    a=i-1
#    hp.mollview(cubo_reconstructed[a,:],title="Reconstructed_Redshift_"+ str(i))
#    print "lendo--> Recontrudted Map Gnilc", a
#    plt.savefig('/share/data1/kfornazier/Analises/Reconstructed_2048/Reconstructed_Cubo_Redshift_'+ str(i) + '.png')
#    pyfits.writeto('/share/data1/kfornazier/Analises/Reconstructed_2048/Reconstructed_Cubo_Redshift_'+str(i)+ '.fits', cubo_reconstructed[a,:])
    

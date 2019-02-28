import h5py
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt

mapa = fits.getdata("free_free_cube_21cm_fore.fits")

hp.mollview(mapa[0,:])
plt.show()
#hp.mollview(a[9,:])
#plt.show()

mapa1 = fits.getdata("ame_cube_21cm_fore.fits")

hp.mollview(mapa1[0,:])
plt.show()


mapa2 = fits.getdata("foreground_cube_21cm_fore.fits")

hp.mollview(mapa2[0,:])
plt.show()


mapa3 = fits.getdata("point_sources_cube_21cm_fore.fits")

hp.mollview(mapa3[0,:])
plt.show()



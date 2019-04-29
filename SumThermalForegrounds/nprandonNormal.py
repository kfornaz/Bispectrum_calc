from scipy.integrate import quad
from scipy.interpolate import interp1d
from scipy.stats import norm
import matplotlib
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
from astropy.io import fits
from math import pi, sin, cos, sqrt, log, floor
from sympy.physics.wigner import gaunt

thermalNoiseFile="mapateste.fits"
foregroundsFile="foreground_cube__bispectrumteste_april.fits"
sumFitsFile="sum.fits"
NSIDE = 128
nchannels=30
valorNside=hp.nside2npix(NSIDE)                                           
mu, sigma = 0, 0.1 # mean and standard deviation 
#freq_min=0.960
#freq_width=10.0
#frequences=freq_min+np.arange(nchannels)*freq_width             
mapa = np.random.normal(mu, sigma, (nchannels,valorNside))
fits.writeto(thermalNoiseFile,mapa)
s = np.random.normal(mu, sigma, (3,2))
thermalNoise=fits.getdata(thermalNoiseFile)
foregrounds=fits.getdata(foregroundsFile)
sum=thermalNoise+foregrounds
fits.writeto(sumFitsFile,sum)
map=fits.getdata(sumFitsFile)
hp.mollview(map[1,:])
plt.show()
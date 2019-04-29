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



def sumFitsMaps(prefix,start,end):
    for i in range(start, end):
        print ("Iniciando mapa " +str(i) )
        thermalNoiseFile= prefix+str(i)+".fits"
        foregroundsFile="foreground_cube__bispectrumteste_april.fits"
        sumFitsFile= "sum"+str(i)+".fits"
        thermalNoise=fits.getdata(thermalNoiseFile)
        foregrounds=fits.getdata(foregroundsFile)
        sum=thermalNoise+foregrounds
        fits.writeto(sumFitsFile,sum)
        print ("Finalizando mapa " +str(i) )


sumFitsMaps("ThermalNoise",0,500)



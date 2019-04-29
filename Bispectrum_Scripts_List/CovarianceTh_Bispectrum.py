# -*- coding: utf-8 -*-

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
from sympy.physics.wigner import wigner_3j
import sys

##############################################################################################################
#This code refers to equation (2.14) of paper arXiv:1509.08107v2.
#The variable c_l11 refers to c_l1 of map 1 and c_l12 refers to c_l1 of map 2, same occurs for the others c_lxx.
#The variable c_l1c refers to cross c_l1 with maps 1 and 2.
#The function B_l refers to the beam transfer function.
#The variable N_l refers to the instrumental noise power spectrum.
##############################################################################################################



#Calculating the beam window function
ls = np.arange(1024)
beam_arcmin = 30.0

def B_l(beam_arcmin, ls):
    theta_fwhm = ((beam_arcmin/60.0)/180.0)*pi #angle in radians
    return np.exp((-0.5*ls*(ls+1)*(theta_fwhm**2))/(8*log(2)))


def calcCovar(nr):
    NSIDE = 64
    mu, sigma = 0, 0.1 # mean and standard deviation
    mapa1 = np.random.normal(mu, sigma, hp.nside2npix(NSIDE))

    NSIDE = 64
    mu, sigma = 0, 0.1 # mean and standard deviation
    mapa2 = np.random.normal(mu, sigma, hp.nside2npix(NSIDE))

    c_l11 = hp.anafast(mapa1, lmax=30)
    c_l21 = hp.anafast(mapa1, lmax=30)
    c_l31 = hp.anafast(mapa1, lmax=30)
    c_l12 = hp.anafast(mapa2, lmax=30)
    c_l22 = hp.anafast(mapa2, lmax=30)
    c_l32 = hp.anafast(mapa2, lmax=30)
    c_l1c = hp.anafast(mapa1, map2=mapa2, lmax=30)
    c_l2c = hp.anafast(mapa1, map2=mapa2, lmax=30)
    c_l3c = hp.anafast(mapa1, map2=mapa2, lmax=30)
    N_l1 = 0
    N_l2 = 0
    N_l3 = 0
    cov = []
    lmax = 30
    l1 = 0
    l2 = 0
    l3 = 0

    for l1 in range(0, lmax+1):
        l2 = l1
        l3 = l1
        cv = 0
        cv = 6*(((2*l1+1)*(2*l2+1)*(2+l3+1))/4*pi)*((wigner_3j(l1,l2,l3,0,0,0))**2)*np.real(((((B_l(0, l1))**2)*c_l11[l1] + N_l1)*(((B_l(0, l1))**2)*c_l12[l1] + N_l1) - ((((B_l(0, l1))**2)*c_l1c[l1])*(((B_l(0, l1))**2)*c_l1c[l1])))*((((B_l(0, l2))**2)*c_l21[l2] + N_l2)*(((B_l(0, l2))**2)*c_l22[l2] + N_l2) - ((((B_l(0, l2))**2)*c_l2c[l2])*(((B_l(0, l2))**2)*c_l2c[l2])))*((((B_l(0, l3))**2)*c_l31[l3] + N_l3)*(((B_l(0, l3))**2)*c_l32[l3] + N_l3) - ((((B_l(0, l3))**2)*c_l3c[l3])*(((B_l(0, l3))**2)*c_l3c[l3]))))
        cov.append(cv)
    np.savetxt("covariance_test"+str(nr)+".txt", cov, delimiter=',')

    ell = np.arange(len(cov))
    plt.rcParams['figure.figsize'] = (12,8) #Normal scale plot.

    plt.xlabel('$\ell$')
    plt.ylabel('$Cov_\ell$')
    plt.plot(ell, cov, 'b.')
    plt.savefig("Covariance_test"+str(nr)+".png")

for i in range (int(sys.argv[1])):
    calcCovar(i)

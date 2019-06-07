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


def calc(nr):
###########################################################################
#This code refers to equation (2.11) of paper arXiv:1509.08107v2.
###########################################################################

    NSIDE = 64
    mu, sigma = 0, 0.1 # mean and standard deviation
    mapa = np.random.normal(mu, sigma, hp.nside2npix(NSIDE))

#####################################################################
# O bloco a seguir é o principal para o calculo da Variância teórica.
#####################################################################
    lmax = 30
    c_l1 = hp.anafast(mapa, lmax=30)
    c_l2 = hp.anafast(mapa, lmax=30)
    c_l3 = hp.anafast(mapa, lmax=30)
    v_ell = []
    l1 = 0
    l2 = 0
    l3 = 0

    for l1 in range(0, lmax+1):
        l2 = l1
        l3 = l1
        v = 0
        v = 6*(((2*l1+1)*(2*l2+1)*(2+l3+1))/4*pi)*((wigner_3j(l1,l2,l3,0,0,0))**2)*np.real(c_l1[l1]*c_l2[l2]*c_l3[l3])
        v_ell.append(v)
    np.savetxt("variance_test"+str(nr)+".txt", v_ell, delimiter=',')
    ell = np.arange(len(v_ell))
    plt.rcParams["figure.figsize"] = (12,8) #Normal scale plot.

    plt.xlabel("$\ell$")
    plt.ylabel("$V_\ell$")
    plt.plot(ell, v_ell, 'b.')
    plt.savefig("Variance_test"+str(nr)+".png")


def calcTotal(nr):
    for i in range(nr):
        calc(i)

calcTotal(int(sys.argv[1]))
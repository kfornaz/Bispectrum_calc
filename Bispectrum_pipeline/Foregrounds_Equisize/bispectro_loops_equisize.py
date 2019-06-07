# encoding: utf-8

##############################################################################
## Algorithm for Bispectrum Calculation      (equisize Triangule)       #####
##                                                                      #####
## Bucher et al  -->  https://arxiv.org/pdf/1509.08107.pdf
## Authors: Karin Fornazier, Filipe Abdalla, Jordany Vieira 
## Email: karin.fornazier@gmail.com
## Supervisor: F.B. Abdalla
## Latest Version June 2019
###########################################################################
###########################################################################

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
import sys


###################################################################################

NSIDE = 128
nchannels=30
valorNside = hp.nside2npix(NSIDE)                                           
mu, sigma = 0, 0.1 # mean and standard deviation 


def anuncio(msg):
    print(msg)
    print("\n")

def gauntB(l1, l2, l3, m1, m2, m3, p1, p2, p3, alm1, alm2, alm3):
    b_ell = gaunt(l1,l2,l3,m1,m2,m3)*np.real(alm1[p1]*alm2[p2]*alm3[p3])
    return b_ell

def alm_position(lmax, la, ma):
    alm_position = hp.Alm.getidx(lmax, la, ma)
    return alm_position

####################################################################################

def belltest(lmax,nrLoops,start,end):

    ## Thermal Noise Maps
    #tot=int(lmax)+1
    #B_elltotal = np.zeros((nrLoops,tot))
    #for i in range(start, end):
    #    mapa = np.random.normal(mu, sigma, (nchannels,valorNside))
    #    fits.writeto('ThermalNoise'+str(i)+".fits", mapa)
    #    print("gerei mapa")

    
    for i in range(start, end):
        mapa = fits.getdata("sum"+str(i)+".fits")# Usar para os mapas do Lucas(Foregrounds)
        print("mapa")    
    ###################################################################################

        B_ell = []
        l1_ell = []
        l2_ell = []
        l3_ell = []

          
        alm1 = hp.map2alm(mapa[1,:])
        alm2 = hp.map2alm(mapa[1,:])
        alm3 = hp.map2alm(mapa[1,:])

    ##################################################################################
### Equiseze conditions

        l0 = 30
        l1 = 0
        l2 = 0
        l3 = 0

        print("Entrei nos fors")
        for l1 in range(0, lmax+1):
            for l2 in range(0, lmax+1):
                for l3 in range(0, lmax+1):
                    if((l1<=l2<=l3) and (abs(l1-l2)<=l3<=abs(l1+l2)) and ((l1+l2+l3)==l0)):
                        anuncio("l1="+str(l1))
                        anuncio("l2="+str(l2))
                        anuncio("l3="+str(l3))
                        l1_ell.append(l1)
                        l2_ell.append(l2)
                        l3_ell.append(l3)
                                                
                        sum=0
                        for m1 in range(-l1, l1+1):
                            p1 = alm_position(lmax, l1, abs(m1))
                            for m2 in range(-l2, l2+1):                    
                                p2 = alm_position(lmax, l2, abs(m2))
                                for m3 in range(-l3, l3+1):                        
                                    p3 = alm_position(lmax, l3, abs(m3))
                                    sum =float(sum)+ gauntB(l1, l2, l3, m1, m2, m3, p1, p2, p3, alm1, alm2, alm3)
                                    

                        anuncio("Valor de saída da Gaunt:")
                        anuncio(float(sum))
                        anuncio("Calculado com valores -> i="+str(i)+" l1="+str(l1)+" l2="+str(l2)+" l3="+str(l3))
                        
                        B_ell.append(sum)
                        
                        anuncio("Estado da matrix B_ell")
                        anuncio(np.array(B_ell))
            
            #nstart=(i-start)
        
            
        print("fim")

    np.savetxt('B_ell_Foregrounds_equisize'+str(i)+".txt", B_ell, delimiter=',')
    #np.savetxt('B_ellRecalculado'+str(i)+".txt", B_ell, delimiter=',')
    np.savetxt('B_ell_ell_Foregrounds_equisize'+str(i)+".txt", np.array([B_ell,l1_ell,l2_ell, l3_ell]).T, delimiter=',')

    return B_ell

####################################################################################
#belltest(lmax,nrLoops,arqName,start,end)
#belltest(30,1,"teste",0,500)

belltest(30,1,0,1)



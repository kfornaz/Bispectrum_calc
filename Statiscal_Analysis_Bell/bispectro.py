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

###################################################################################

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

def belltest(lmax,nrLoops,arqName,start,end):
    tot=int(lmax)+1
    B_elltotal = np.zeros((nrLoops,tot))
    for i in range(start, end):
        
        NSIDE = 64
        mu, sigma = 0, 0.1 # mean and standard deviation
        mapa = np.random.normal(mu, sigma, hp.nside2npix(NSIDE))
        print "gerei mapa"
    ###################################################################################

        B_ell=[]
        
        alm1 = hp.map2alm(mapa)
        alm2 = hp.map2alm(mapa)
        alm3 = hp.map2alm(mapa)
        sum = 0

    ##################################################################################

        l1 = 0
        l2 = 0
        l3 = 0

        for l1 in range(0, lmax+1):
            anuncio("l1="+str(l1))
            l2 = l1
            l3 = l1
            for m1 in range(-l1, l1+1):
                
                p1 = alm_position(lmax, l1, abs(m1))
                for m2 in range(-l1, l1+1):
                    
                    p2 = alm_position(lmax, l1, abs(m2))
                    for m3 in range(-l1, l1+1):
                        
                        p3 = alm_position(lmax, l1, abs(m3))
                        sum += gauntB(l1, l2, l3, m1, m2, m3, p1, p2, p3, alm1, alm2, alm3)
                        anuncio("i="+str(i)+" l1="+str(l1)+" m1="+str(m1)+" m2="+str(m2)+" m3="+str(m3))
                        
            B_ell.append(sum)
            sum = 0
            nstart=(i-start)
        
            
        print("fim")

        np.savetxt('B_ell'+str(i)+".txt", B_ell, delimiter=',') 
    return B_ell

####################################################################################







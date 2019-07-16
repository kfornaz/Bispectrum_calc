#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script calculates Cls and power spectrum from
two maps (usually one is 21cm and the other one is the reconstructed map
from gnilc

Developed by Alessandro Marins and K. Fornazier
July 2019
"""

import os
import math
import numpy as np
import healpy as hp
from astropy.io import fits
import matplotlib.pyplot as plt

path     = os.getcwd()
path_in  = os.path.join(path,"input")
path_out = os.path.join(path,"output")

dir_in = os.listdir(path_in)
dir_out = os.listdir(path_out)
dir_in
dir_out

path_map_in  = os.path.join(path_in,dir_in[0])     #coloque o índice do mapa 21cm flask
path_map_out = os.path.join(path_out,dir_out[0]) #coloque o índice do mapa reconstruído

map_in  = fits.getdata(path_map_in)[1,:]
map_out = fits.getdata(path_map_out)[1,:]

cl_in = hp.anafast(map_in)
cl_out = hp.anafast(map_out)
l_in = np.arange(len(cl_in))
l_out = np.arange(len(cl_out))

fig, ((ax1, ax2, ax3)) = plt.subplots(1,3)
ax1.plot(l_in, cl_in,"r") 
ax1.grid()

ax2.plot(l_out, cl_out,"b")
ax2.grid()

ax3.plot(l_in, cl_in,"r") 
ax3.plot(l_out, cl_out,"b")
ax3.grid()

plt.savefig('clscompare.png')

pi=math.pi
dl_in=(l_in*(l_in+1)*cl_in)/(2*pi)
dl_out=(l_out*(l_out+1)*cl_out)/(2*pi)

fig, ((ax4, ax5, ax6)) = plt.subplots(1,3)
ax4.loglog(dl_in, l_in,"r") 
ax4.grid()

ax5.loglog(dl_out, l_out,"b")
ax5.grid()

ax6.loglog(l_in, cl_in,"r") 
ax6.loglog(l_out, cl_out,"b")
ax6.grid()

plt.savefig('espectrodepotencia.png')
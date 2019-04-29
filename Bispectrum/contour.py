from mpl_toolkits.mplot3d import Axes3D
from stats import getCovMatrix
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
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
import stats
import setupcov

def getArq(i,prefix):
    return prefix+str(i)+ext

def generateGraph(title,prefix,sb1,sb2,sb3):
   
    
    matrix=np.array([stats.carregarMedia(getArq(i,prefix)) for i in range(start,end)]) 
    
    print(matrix.shape)
    
    ysize=matrix.shape[0]#get the x dimension form matrix shape (erro do numpy, precisei inverter)
    xsize=matrix.shape[1]#get the y dimension form matrix shape
   
    X = np.arange(xsize)#set the x dimension form matrix shape
    xlen = len(X)
    Y = np.arange(ysize)#set the y dimension form matrix shape
    ylen = len(Y)
    #X, Y = np.meshgrid(X, Y)#set the grid
    Z = matrix #set z value from Bell
    
    plt.subplot(sb1,sb2,sb3)    
    cp = plt.contourf(X, Y, Z,cmap=cm.YlOrRd)
    plt.colorbar(cp)
    plt.title(title)
    plt.xlabel('l1=l2=l3')
    plt.ylabel('l1=l2=l3')
    
    
    mean=matrix.mean()
    std=matrix.std()
    max=np.amax(matrix)
    min=np.amin(matrix)
    print("Mean: "+str(mean))
    print("STD: "+str(std))
    print("Max: "+str(max))
    print("Min: "+str(min))
   
    


#load setup parameters
titleForeg='Bi Spectrum teste - Foregrounds'
titleThermal='Bi Spectrum teste - Thermal'
prefixForeg="B_ellSum"
prefixThermal="B_ell"
ext=".txt"
start=0
end=500
lmax=31





plt.figure(figsize=(21, 10))
generateGraph(titleThermal,prefixThermal,1,2,1)
generateGraph(titleForeg,prefixForeg,1,2,2)
plt.show()







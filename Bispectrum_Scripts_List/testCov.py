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

#load setup parameters
prefix=setupcov.prefix
start=setupcov.start
end=setupcov.end
#matrix=stats.getCovMatrix(prefix,start,end) do no use this the matrix i already done
matrix=stats.carregarMedia(setupcov.prefixMatrix)#get the covariation matrix
mean=matrix.mean()
std=matrix.std()
max=np.amax(matrix)
min=np.amin(matrix)


xsize=matrix.shape[0]#get the x dimension form matrix shape
ysize=matrix.shape[1]#get the y dimension form matrix shape

#3D Graph
fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(xsize)#set the x dimension form matrix shape
xlen = len(X)
Y = np.arange(ysize)#set the y dimension form matrix shape
ylen = len(Y)
X, Y = np.meshgrid(X, Y)#set the grid
Z = matrix#set z axis from Cov Matrix
colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[x, y] = colortuple[(x + y) % len(colortuple)]

surf = ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0)

ax.set_zlim(0.25*min,.25*max)
ax.w_zaxis.set_major_locator(LinearLocator(6))

plt.show()
print(mean)
print(std)
print(max)
print(min)
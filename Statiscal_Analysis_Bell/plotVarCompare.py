import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
import util
import pylab as pl
from io import StringIO 

def getPlotVarCompare(prefix,start,end):
    th_var=np.loadtxt(prefix+str(start)+".txt")
    for i in range(start+1,end):
        th_var= np.concatenate((th_var,np.loadtxt(prefix+str(i)+".txt")),axis=0)
        plt.plot(np.arange(len(th_var)), th_var,'o') 
        pl.xlabel('multipole')
        pl.ylabel('Variance')
        pl.xlim(-5.0,500)
    #pl.ylim(-10,10-17)
    plt.show()


getPlotVarCompare("variance_test",0,499)

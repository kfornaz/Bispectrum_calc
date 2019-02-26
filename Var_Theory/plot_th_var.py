# -*- coding: utf-8 -*-
"""
Script for plotting variance. It reads several files txt and plot
its values
USAGE:   python plot_th_var.py

Need to be translated --> some functions were written in Portuguese
Written by: K. S.F. Fornazier, on jan-2019., on jan-2019.
"""

import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
import util
from io import StringIO 


def getPlotThCovar(prefix,start,end):
    th_var=np.loadtxt(prefix+str(start)+".txt")
    for i in range(start+1,end):
        th_var= np.concatenate((th_var,np.loadtxt(prefix+str(i)+".txt")),axis=0)
    plt.plot(np.arange(len(th_var)), th_var,'o')    
    plt.show()


getPlotThCovar("variance_test",0,499)

# -*- coding: utf-8 -*-
"""
This script calculates the covariance matrix

USAGE:   python CovMatrix.py

Written by: Karin S. F. Fornazier  karin.fornazier@gmail.com, on jan-2019.
"""
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
import util
from io import StringIO 

## It calculates covariance of two files (B_ell_number.txt)
## Remembering cov=np.cov(x,y)[0,1], where [0,1] takes just the line 1 column2 as explained here:
##The covariance matrix can be calculated in NumPy using the cov() function. By default, this function will calculate the sample covariance matrix.
# The cov() function can be called with a single matrix containing columns on which to calculate the covariance matrix, or two arrays, 
# such as one for each variable.

def getCovValues(prefix,i,j):
    x=np.loadtxt(prefix+str(i)+".txt")
    y=np.loadtxt(prefix+str(j)+".txt")
    cov=np.cov(x,y)[0,1]
             
    return cov

def getMatrizJordany(start,end,prefix):
    size=end-start
    sizeTotal=pow(size,2)
    print(sizeTotal)
    Jordany=np.zeros((size,size),dtype=float)
     
    for i in range(start,end):
        for j in range(start,end):
            Jordany[i,j]=getCovValues(prefix,i,j)           
            print("("+str(i)+","+str(j)+")")
            plt.plot(i*j,Jordany[i,j],'o')        
    np.savetxt('matrizCovteste.txt', Jordany, delimiter=',')
    plt.show()
    return Jordany

## 3 parameters
## start == first B_ell
## end == last B_ell
## prefix == B_ell

getMatrizJordany(0,500,"B_ell")
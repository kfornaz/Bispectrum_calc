# -*- coding: utf-8 -*-
"""
This module calculates mean and std from
all Bell*.txt (each map generates 30 -lmax- Bell values)

It is used by calcMedia.py

> nrLoopStart = first file read
> nrLoopStart = last file read
> arqIn - prefix of this file
> arqOut - final file where we write  mean and std


Written by: Edvaldo B. Guimarães, on jan-2019.
"""
import numpy as np
import util

def meanstd(nrLoopStart,nrLoopEnd,arqIn,arqOut): 
    util.write2Dsk(arqOut,"i,mean,std\n")
    for i in range(nrLoopStart,nrLoopEnd):
        B_elltotal=np.loadtxt(arqIn+str(i)+".txt")
        mean=np.mean(B_elltotal, dtype=np.float64)
        print "mean_map ==", mean
        std=np.std(B_elltotal, dtype=np.float64)
        print "std_map ==", std
        util.write2Dsk(arqOut,str(i))
        util.write2Dsk(arqOut,",")
        util.write2Dsk(arqOut,str(mean))
        util.write2Dsk(arqOut,",")
        util.write2Dsk(arqOut,str(std))
        util.write2Dsk(arqOut,"\n")
        
        
    

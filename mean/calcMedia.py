# -*- coding: utf-8 -*-
"""
This script calculates mean and std from
all Bell*.txt (each map generates 30 -lmax- Bell values), 
calling module mean.py

> python calcMedia.py 0 500 B_ell filename.txt

Where B_ell means prefix over all txt files between 0 and 500

Written by: Edvaldo B. Guimarães, on jan-2019.
"""
import mean as media
import os
import sys
import util

## nLoopStart = initial file (in the example is number 0)
## nLoopEnd   = final file (in the example is number 500)
## arqIn      = prefix read B_ell_number.txt
## arqOut     = file final name 

ext=".txt"

nrLoopStart=int(sys.argv[1]) 
nrLoopEnd=int(sys.argv[2])
arqIn=(sys.argv[3])
arqOut=(sys.argv[4])

media.meanstd(nrLoopStart,nrLoopEnd,arqIn,arqOut)


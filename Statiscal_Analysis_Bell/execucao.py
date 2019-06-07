# -*- coding: utf-8 -*-
"""
This script calls bispectrum script and is used in execBat.py

Written by: Edvaldo B. Guimarães, on jan-2019.
"""

import bispectro as bi
import sys
from tempfile import TemporaryFile
import numpy as np
import util



util.printTime("Initializing i="+sys.argv[1])

## lmax = 30, 1 loop (because is paralelized and independent), thermal noise map , 0 (initial) related to the first for in the bispectrum function, 
# 1 (end) related to the end of this for in the bispectrum function
 
result=bi.belltest(30,1, sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))


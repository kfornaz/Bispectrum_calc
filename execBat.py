# -*- coding: utf-8 -*-
"""
This script paralelizes the generation of maps.
For generating 500 maps, we should type:

> python execBat.py 0 500

It is necesssary to run it in a clean directory.

Written by: Edvaldo B. Guimarães, on jan-2019.
"""
import os
import sys
import util

## String build to comand execution. This one uses 8 core processors

comando="taskset -c 0,1,2,3,4,5,6,7 python execucao.py"
comandoTotal=comando

##uses the module util, which has non-calc functions, such as write in disk:
util.writeDsk("inicioBat.txt","Initializing...")


for i in range (int(sys.argv[1]),int(sys.argv[2])):
   

 comandoTotal=comando+" ParalelTest"+str(i)+" "+str(i)+" "+str(i+1)+" & "

 print comandoTotal

 os.system(comandoTotal) 





import sys
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
from io import StringIO 

# getBell reads all txt files (which have Bell vector results) and concatenate
# where each Bell file will be a new column. 
def readBellTxt(prefix,i):         
    matrixBell=np.loadtxt(prefix+str(i)+".txt")
    return matrixBell
  

def getBell(prefix,start,end):
    sizeRow=31
    sizeCollun=500
    matrixBell=np.zeros((sizeRow,sizeCollun),dtype=float)
    print(matrixBell.size)
    print(matrixBell.shape)
    for i in range(start,end):
        matrixBellActual=readBellTxt(prefix,i)
        for j in range(sizeRow):
            print(str(j)+","+str(i))
            
            matrixBell[j,i]=matrixBellActual[j]
    np.savetxt("matrix"+prefix+".txt",matrixBell)


def calculateMatrixBellMean(arq,arqMedia):
    matrixBell=np.loadtxt(arq) 
    matrixBellMean=np.mean(matrixBell,axis=1)
    np.savetxt(arqMedia,matrixBellMean)
    

    
   
   

     
    









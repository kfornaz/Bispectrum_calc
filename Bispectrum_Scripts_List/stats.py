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

def loadFile(arq):
    matrix=np.loadtxt(arq)
    return matrix

def calculateMatrixBellMean(matrixBell,arqMedia):    
    matrix=np.mean(matrixBell,axis=1)
    np.savetxt(arqMedia,matrix)
    return matrix

def calculateMatrixBellStd(matrixBell,arqMedia):    
    matrix=np.std(matrixBell,axis=1)
    np.savetxt(arqMedia,matrix)
    return matrix

def calculateMatrixBellVar(matrixBell,arqMedia):    
    matrix=np.var(matrixBell,axis=1)
    np.savetxt(arqMedia,matrix)
    return matrix

def criarImg(conjGraf):
    plt.clf()
    for j in conjGraf:
        ell = np.arange(j[0].size)        
        plt.xlabel('$\ell$')
        plt.ylabel('$B_\ell$')
        l=plt.plot(ell, j[0],'o',label=j[1],color=j[2],marker=j[3])
        plt.setp(l, markersize=5)
        plt.ylim(j[4])
        plt.xlim((-1, j[0].size))
        plt.style.use('classic')
        plt.legend(fontsize=12)
    
    plt.show()
    salvarPLT(plt,"Both.png")  
    
    
def salvarPLT(plt,nome):
   
    plt.savefig(nome)


def carregarMedia(arqIn):
    dados=np.loadtxt(arqIn)
    return dados


def getCovMatrix(prefix,start,end):    
    matrix=np.array([[getCovValues(prefix,i,j) for i in range(start,end)] for j in range(start,end)])    
    print (matrix.size)
    print(matrix.shape)
    arqMedia=prefix+"MatrixCov.txt"
    np.savetxt(arqMedia,matrix)
    return matrix

def getCovMatrixFlat(matrix):
    matrix.ravel()
    return matrix.ravel()



def getCovValues(prefix,i,j):
    x=np.loadtxt(prefix+str(i)+".txt")
    y=np.loadtxt(prefix+str(j)+".txt")
    cov=np.cov(x,y)[0,1]
    print("Executando item"+str(i)+","+str(j))
    print("Variance: "+prefix+str(i))
    print(np.var(x))                 
    print("Variance: "+prefix+str(j))
    print(np.var(y))                 
    print("Covariance Matrix: "+prefix+str(i)+","+prefix+str(j))
    print(np.cov(x,y))
    return cov


def workflow():
    #InitialSetup - Name Prefix and Sufix seted to avoid repetiton
    start=0
    end=500
    size=end-start
    prefix="matrixB_ellSum"
    prefixCov="B_ellSum"
    fileExt=".txt"
    graphicLegendSufix= "Foregrounds + Thermal Noise"
    arq=loadFile(prefix+fileExt) #Origin Matrix with 500x500
    arqMediaMean=prefix+"Mean"+fileExt #Mean TXT filename
    arqMediaStd=prefix+"Std"+fileExt #STD TXT filename
    arqMediaVar=prefix+"Var"+fileExt #VAR TXT filename

    #Step 1 - Calculate Mean,STD,Var,Covar
    MatrixBellMean=calculateMatrixBellMean(arq,arqMediaMean)
    MatrixBellStd=calculateMatrixBellStd(arq,arqMediaStd)
    MatrixBellVar=calculateMatrixBellVar(arq,arqMediaVar)
    MatrixBellCov=getCovMatrix(prefixCov,start,end)

    #Step 2 - GenerateImageMaps
    criarImg([[MatrixBellMean,"Mean "+graphicLegendSufix,"r","o",(-200, 800)]])
    criarImg([[MatrixBellStd,"STD "+graphicLegendSufix,"g","o",(-0.5, 0.5)]])
    criarImg([[MatrixBellVar,"Var "+graphicLegendSufix,"b","o",(-0.15, 0.15)]])
    matrix=getCovMatrixFlat(MatrixBellCov)
    criarImg([[matrix,"Covariance "+graphicLegendSufix,"r","o",(3.1770e+09,3.17795e+09)]])

    









     
    









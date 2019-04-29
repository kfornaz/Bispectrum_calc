import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
from io import StringIO 



def criarImg(conjGraf):
    for j in conjGraf:
        ell = np.arange(j[0].size)        
        plt.xlabel('$\ell$')
        plt.ylabel('$B_\ell$')
        l=plt.plot(ell, j[0],'o',label=j[1],color=j[2],marker=j[3])
        plt.setp(l, markersize=5)
        plt.ylim((-200, 800))
        plt.xlim((-1, 32))
        plt.style.use('classic')
        plt.legend(fontsize=12)
    
         
   
    
    plt.show()
    salvarPLT(plt,"Both.png")  
    
    
def salvarPLT(plt,nome):
   
    plt.savefig(nome)


def carregarMedia(arqIn):
    dados=np.loadtxt(arqIn)
    return dados


meanBell=carregarMedia("matrixB_ellMean.txt")
meanBellSum=carregarMedia("matrixB_ellSumMean.txt")


#criarImg([[meanBell,"Thermal Noise","y","o"],[meanBellSum,"Foregrounds + Thermal Noise","r","o"]])

criarImg([[meanBellSum,"Foregrounds + Thermal Noise","r","o"]])






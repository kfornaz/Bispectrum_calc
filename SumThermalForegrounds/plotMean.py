import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
import util
from io import StringIO 
from numba import cuda, float32
TPB = 16



def criarImg(conjGraf):
    for j in conjGraf[0]:
        ell = np.arange(len(j))        
        plt.xlabel('$\ell$')
        plt.ylabel('$B_\ell$')
        if len(conjGraf)>1:
            l=plt.plot(ell, j,'o',label=conjGraf[1],color=conjGraf[2],marker=conjGraf[3])
        else:
            l=plt.plot(ell, j,'o')
        plt.setp(l, markersize=0.5) 
        plt.style.use('classic')
        plt.legend(fontsize=6)
        
    return plt   
    
    
def salvarPLT(plt,nome):
    plt.show()
    plt.savefig(nome)


def carregarMedia(arqIn):
    dados=open(arqIn).readlines(  )
    count = len(dados)
    print("lendo Arquivo de "+str(count)+" Linhas")
    return dados
# -*- coding: utf-8 -*-
"""
Module used for all functions used to plot bispectrum info, such as covariance, variance 
and plotting these graphs.

USAGE:   import scatterplot

Need to be translated --> some functions were written in Portuguese
Written by: Edvaldo B Guimaraes, on jan-2019., on jan-2019.
"""

import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
import util
from io import StringIO 

## This function creates a plt image 


## conjGraph[0] == it is an array of arrays with all numerical data (mean, std, etc. etc)
## conjGraph[1] == label
## conjGraph[2] == color
## conjGraph[3] == marker
## conjGraph[4] == markersize
## ell --> axis x

def criarImg(conjGraf,labelX,labelY):
    for j in conjGraf[0]:
        ell = np.arange(len(j))                
        if len(conjGraf)>1:
            l=plt.plot(ell, j,'o',label=conjGraf[1],color=conjGraf[2],marker=conjGraf[3])
            plt.setp(l, markersize=conjGraf[4])        
            plt.style.use('classic')
            plt.legend(fontsize=6)
        else:
                             
            l=plt.plot(ell, j,'o',color=np.random.rand(1,4)[0])        
        
        
    return plt   
    

 ## This function creates a plot for covariance matrix --> read a .txt with this data  
 #  
def criarImgCov(conjGraf):
    for j in conjGraf[0]:
        ell = np.arange(len(j)) 
        size=len(j)       
        plt.xlabel('$\ell$')
        plt.ylabel('$B_\ell$')
        l=plt.plot(j,'o',label=conjGraf[1],color=conjGraf[2],marker=conjGraf[3])        
        plt.setp(l, markersize=0.5) 
        plt.style.use('classic')
        plt.legend(fontsize=6)
        
    return plt   
    
## Save this plt   
def salvarPLT(plt,nome):
    plt.savefig(nome)
    plt.show(nome)

## Receives a file name and returns a nparray

def carregarMedia(arqIn):
    dados=open(arqIn).readlines(  )
    count = len(dados)
    print("Reading File  "+str(count)+"lines")
    return dados

## Reads files csv with mean and std. Returns mean, std and variance in separate files
## arqIn = file full name, example mean.txt
## arqOutMean = prefix to final file

def getPlotMeanVariance(arqIn,arqOutMean):
    dados=carregarMedia(arqIn)
    for l in (dados):
        linhaDados=l.split(",")
        mean=linhaDados[1]
        std=linhaDados[2]
        variance=pow(float(linhaDados[2]),2)
        util.write2Dsk(arqOutMean+".txt",mean+"\n")
        util.write2Dsk(arqOutMean+"std.txt",std)    
        util.write2Dsk(arqOutMean+"var.txt",str(variance)+"\n")    
    
    conjGraficos=[[np.loadtxt(arqOutMean+".txt")],"Mean",'b','o']
    salvarPLT(criarImg(conjGraficos),arqOutMean+"mean.png")

    conjGraficos=[[np.loadtxt(arqOutMean+"std.txt")],"std",'c','x']
    salvarPLT(criarImg(conjGraficos),arqOutMean+"std.png")

    conjGraficos=[[np.loadtxt(arqOutMean+"var.txt")],"Var",'y','o']
    salvarPLT(criarImg(conjGraficos),arqOutMean+"var.png")

    conjGraficos=[[np.loadtxt(arqOutMean+".txt"),np.loadtxt(arqOutMean+"std.txt"),np.loadtxt(arqOutMean+"var.txt")],"",'r','x']         
    salvarPLT(criarImg(conjGraficos),arqOutMean+"both.png")

## This polimorphym function reads same files in the same time. Equal previous function, despites the initial condition

def getPlotMeanVariance(prefix,start,end):        
    pontos=np.loadtxt(prefix+str(start)+".txt")
    for i in range(start+1,end):        
      pontos= np.concatenate((pontos,np.loadtxt(prefix+str(i)+".txt")),axis=0)
    
    conjGraficos=[[pontos],"Todos",'b','o']    
    salvarPLT(criarImg(conjGraficos),prefix+"Variance.png")

## Gets covariance
def getPlotCoVariance(arq):            
    conjGraficos=[[np.loadtxt(prefix+str(start)+".txt")],"Matriz de Covariancia",'b','o']    
    salvarPLT(criarImg(conjGraficos),prefix+"CovarianceMatrix.png")

## gets variance

def getVariance(arq):
    varArray=np.loadtxt(arq)    
    return varArray

## gets matriz "jordany" --> Os elementos da diagonal da matriz serao a variancia de cada B_ell (cada mapa), isto e, o elemento 0,0 da matriz
## sera a variancia do B_ell0 e o elemento 499,499 sera a variancia do B_ell499.
## Os demais elementos serão a covariancia entre dois B_ell diferentes, ou seja, o elemento 0,1 sera a Cov(B_ell0,B_ell1)
##, naquela formula X=B_ell0 e Y=B_ell1.

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
    np.savetxt('matrizCov.txt', Jordany, delimiter=',')
    plt.show()
    return Jordany

## Receives a matrix called Jordany and plots covariance matrix, point by point
## matplotlib crashes when we use plt show -- need to try using plt save

def getMatrizJordany1(Jordany):
    size=len(Jordany)
    sizeTotal=pow(size,2)
    print(str(sizeTotal))    
    ell = np.arange(sizeTotal)
    contador=0   
    for i in range(0,size):
        for j in range(0,size):                 
            contador=contador+1
            print("("+str(i)+","+str(j)+")")
            plt.plot(contador,Jordany[i,j],'o')        
    np.savetxt("matrizCov"+str(sizeTotal)+".txt", Jordany, delimiter=',')
    plt.show()
    return Jordany


##Receives data and make a covariance between two values -each bell from each txt 
## returns a value (not a vector) as "A covariance value of zero indicates that both variables
## are completely independent. NumPy does not have a function to calculate the covariance between
## two variables directly. Instead, it has a function for calculating a covariance matrix called cov()
## that we can use to retrieve the covariance." described in:https://machinelearningmastery.com/introduction-to-expected-value-variance-and-covariance/

def getCovValues(prefix,i,j):
    x=np.loadtxt(prefix+str(i)+".txt")
    y=np.loadtxt(prefix+str(j)+".txt")
    cov=np.cov(x,y)[0,1] 
             
    return cov

## Plots covariance matrix
def getPlotCovMatrix(covMatrix):
    conjGraficos=[[covMatrix],"",'b','o']    
    salvarPLT(criarImgCov(conjGraficos),"CovarianceMatrix.png")

## Plot Covariance
def getPlotCovariance(prefix,x):
    covValues=np.zeros(x)
    for i in range(x):
        j=i+1
        covValues[i]=getCovValues(prefix,i,j)

    plt.plot(covValues, 'o')
    print covValues
    plt.xlabel('$Covariance$')
    plt.ylabel('$B_\ell$')
    plt.show()


def getPlotCovMatrixLoad(arq):
    matrix=np.loadtxt(arq,delimiter=',').ravel()
    return matrix

def getPlotCovMatrixFlat(matrix):
    conjGraficos=[[matrix]]    
    plt.xlabel('Covariance Matrix Combination Number')
    plt.ylabel('Covariance Values')
    salvarPLT(criarImg(conjGraficos,"$B_\ell$","$B_\Cov$"),"ResultMatrix.png")

def getPlotVarFlat(matrix,eixox,eixoy, nome):
    conjGraficos=[[matrix]]    
    plt.xlabel(eixox)
    plt.ylabel(eixoy)
    salvarPLT(criarImg(conjGraficos,eixox,eixoy),nome)        







    

    


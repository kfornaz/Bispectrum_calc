# -*- coding: utf-8 -*-
"""
Module used for all functions used to plot bispectrum info, such as covariance, variance 
and plotting these graphs.

USAGE:   python scatterplot.py

Need to be translated --> some functions were written in Portuguese
Written by: Edvaldo B Guimaraes, on jan-2019., on jan-2019.
"""
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

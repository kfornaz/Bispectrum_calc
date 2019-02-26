import numpy as np
import pylab as pl


data1=np.loadtxt('var.txt')
data2=np.loadtxt('variance_test0.txt')
data3=np.loadtxt('variance_test1.txt')
data4=np.loadtxt('variance_test2.txt')
data5=np.loadtxt('variance_test3.txt')
data6=np.loadtxt('variance_test4.txt')
data7=np.loadtxt('variance_test5.txt')
data9=np.loadtxt('variance_test6.txt')
eixo=np.arange(499)
eixo2=np.arange(31)

pl.plot(eixo2,data4,'ro')
pl.plot(eixo2,data2,'co')
pl.plot(eixo2,data3,'bo')
pl.plot(eixo2,data5,'bo')
pl.plot(eixo2,data6,'bo')
pl.plot(eixo2,data7,'bo')
#pl.plot(eixo,data1,'bo')


pl.xlabel('multipole')
pl.ylabel('Variance')
pl.xlim(-5.0,35.)
pl.show()
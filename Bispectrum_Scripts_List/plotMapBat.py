"""
Receives .txt file which contains a covariance matrix and plot its results
using matplot lib


USAGE:   python plotMapBat.py name.txt

Written by: Karin S. F. Fornazier  karin.fornazier@gmail.com, on jan-2019.
"""
import scatterplot
import sys


MATRIZ=scatterplot.getPlotCovMatrixLoad(sys.argv[1])
scatterplot.getPlotCovMatrixFlat(MATRIZ)

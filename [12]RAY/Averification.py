#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Script for post-processing acceleration time histories
resulting from the ray visualizer in the elastic calculator
"""
from __future__ import division
from os import sys
sys.path.append('../CALCULATOR/')
import matplotlib.pyplot as plt
import numpy as np
import signals as sig
#
# Process input motion
#
plt.figure(0)
dt = 0.077
fs = 10.0
DATOS = np.loadtxt('respuesta.txt' )
ninc = 129
signal=np.zeros([ninc , 71], dtype=float)
k = 0
for j in range(5 , 75):
    for i in range(ninc):
        signal[i , k ] =  DATOS[j , i] + k/5
    sig.grafsignalG(signal[: , k] , 'salida' , 'Displacement' , 'l' , 0.0 , 20.0 , dt , 0)
    k = k+1
#    x, Samag , A , nfs = sig.Ftrans(signal[: , k] , 129 , dt , fs)
#    sig.grafFourier(Samag , x , nfs , 'Fourier', 0.0 , 0.0 , 0.0 , 0.0 , 1)
#       k = k+1
#sig.grafsignalG(signal[: , 5] , 'salida' , 'Displacement' , 'l' , 0.0 , 20.0 , dt , 2)
#x, Samag , A , nfs = sig.Ftrans(signal[: , 5] , 129 , dt , fs)
#sig.grafFourier(Samag , x , nfs , 'Fourier', 0.0 , 0.0 , 0.0 , 0.0 , 4)

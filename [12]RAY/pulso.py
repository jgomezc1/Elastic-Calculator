# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:36:56 2015

@author: eafit
"""
import numpy as np
from os import sys
sys.path.append('../CALCULATOR/')
import signals as sig
import matplotlib.pyplot as plt
from sympy import init_printing
init_printing()
"""
Creates model.
"""
dt = 0.025
Tt = 8.0
tc = 4.0
nt = int(Tt / dt )
fc = 1.0

Rick, time = sig.ricker(nt , Tt, tc, fc)
plt.plot(time , Rick)
x , Samag , A , nfs = sig.Ftrans(Rick , nt , dt , Tt)
sig.grafFourier(Samag , x , nfs , 'FAS', 0.0 , 8.0 , 0.0 , 5.0 , 2)

#np.savetxt('respuesta.txt' , SOL )

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
fc = 4.0
Tt = 2.0/fc
tc = Tt/2
dt = 0.0005
nt = int(Tt / dt )

Rick, time = sig.ricker(nt , Tt , tc, fc)
plt.plot(time , Rick)
x , Samag , A , nfs = sig.Ftrans(Rick , nt , dt , Tt)
sig.grafFourier(Samag , x , nfs , 'FAS', 0.0 , 4.0 , 0.0 , 0.2 , 2)

#np.savetxt('respuesta.txt' , SOL )

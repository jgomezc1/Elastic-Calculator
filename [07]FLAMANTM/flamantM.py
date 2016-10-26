# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:36:56 2015

@author: eafit
"""
import numpy as np
from os import sys
sys.path.append('../CALCULATOR/')
from sympy import init_printing
init_printing()
import elasticity as ela
import plotter as plo
import generategeo as geo

"""
Creates mesh files.
"""
phid = 45.
phi  = ela.radianes(phid)
l = np.sqrt(1.)
var = geo.wedge(l , phid, 0.1)
nodes , elements , nn =geo.create_model(var )
coords=np.zeros([nn,2])
SOL = np.zeros([nn , 2])
"""
Computes the solution
"""
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
m = 1.0
height = np.amax(coords[:,1])
for i in range(0,nn):
    X = coords[i,0]
    Y = coords[i,1]
    y = X
    x = Y - height 
    sigmar , sigmat =ela.flamantM(x , y , m , phid)
    SOL[i, 0] = sigmar
    SOL[i, 1] = sigmat
"""
Plot the solution
"""
plo.plot_stress(SOL , nodes , elements , plt_type ="contourf",  levels = 24 )
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:36:56 2015

@author: eafit
"""
import numpy as np
from os import sys
sys.path.append('../CALCULATOR/')
import plotter as plo
import generategeo as geo
import elasticity as ela
from sympy import init_printing
init_printing()
"""
Creates model.
"""
ninc = 4097
r = 1.0
l = 6.0
h = 3.0
c = 0.15
var = geo.canyon(r, l, h, c)
nodes , elements , nn =geo.create_model(var , False)
plo.viewmesh(nodes , elements , True)
"""
Define solution arrays
"""
coords=np.zeros([nn,2])
SOL = np.zeros([nn,ninc])
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
"""
Computes the solution
"""
for i in range(nn):
    x = coords[i,0]
    y = coords[i,1]
    u = ela.trifunac(x , y )
    for j in range(ninc):
        SOL[i,j] = u[j]
#
# Plot the solution
#
#plo.plot_SFIELD(SOL[:,  0], nodes, elements , 1 , plt_type="contourf",  levels=12)


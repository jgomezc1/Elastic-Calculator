# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:36:56 2015

@author: eafit
"""
import numpy as np
import elasticity as ela
import plotter as plo
import generategeo as geo
from sympy import init_printing
init_printing()
"""
Creates mesh files.
"""
phid = 45.
phi  = ela.radianes(phid)
l = np.sqrt(32.)
var = geo.wedge(l , phid, 0.1)
nodes , elements , nn =geo.create_model(var)
coords=np.zeros([nn,2])
SOL = np.zeros([nn])
#
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]

"""
Computes the solution
"""
q = 1.0
height = np.amax(coords[:,1])
for i in range(0,nn):
    X = coords[i,0]
    Y = coords[i,1]
    y = X
    x = Y - height
    sigma =ela.flamantQ(x , y , q , phid)
    SOL[i] = sigma
"""
Plot the solution
"""
plo.plot_UVAR(SOL, nodes , elements , plt_type ="contourf",  levels = 24 )
#
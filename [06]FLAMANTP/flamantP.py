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
phid = 40.
phi  = ela.radianes(phid)
l = np.sqrt(1.0)
var = geo.wedge(l , phid, 0.1)
nodes , elements , nn =geo.create_model(var , False)
coords=np.zeros([nn,2])
SOL = np.zeros([nn])
"""
Computes the solution
"""
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
p = 10.0
height = np.amax(coords[:,1])
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1]
    Y = x
    X = height-y
    sigma =ela.flamantP(X , Y , p , phid)
    SOL[i] = sigma
"""
Plot the solution
"""
plo.plot_SFIELD(SOL, nodes , elements , 1 , plt_type ="contourf",  levels = 24 )
plo.viewmesh(nodes , elements , view = True)
#
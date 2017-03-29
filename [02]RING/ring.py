# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:36:56 2015

@author: eafit
"""
import numpy as np
from os import sys
sys.path.append('../CALCULATOR/')
import elasticity as ela
import plotter as plo
import generategeo as geo
from sympy import init_printing
init_printing()
"""
Creates model.
"""
a = 2.0
b = 3.0
var = geo.ring(a , b , 0.1 )
nodes , elements , nn =geo.create_model(var , False)
"""
Define solution arrays
"""
coords=np.zeros([nn,2])
SOL = np.zeros([nn , 2])
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
"""
Define pressures (a: internal; b external)
"""
pa =  1.0
pb =  2.0
"""
Computes the solution
"""
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1] 
    sigmar , sigmat =ela.prering(x , y , a , b , pa , pb)
    SOL[i, 0] = sigmar
    SOL[i, 1] = sigmat
#
# Plot the solution
#
plo.plot_stress(SOL , nodes , elements ,1, plt_type ="pcolor",  levels = 12 )
plo.viewmesh(nodes , elements , True)
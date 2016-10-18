# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:36:56 2015

@author: eafit
"""
import numpy as np
import elasticity as ela
import plotter as plo
from sympy import init_printing
init_printing()
#
# reads nodes and elements files
#
nodes        = np.loadtxt('nodes.txt')
elements     = np.loadtxt('eles.txt')
nn =len(nodes[:,0])
coords=np.zeros([nn,2])
SOL = np.zeros([nn , 2])
#
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
height = np.amax(coords[:,1])
#
# Define solution parameters
#
a = 1.5
b = 2.0
pa = -5.0
pb = 10.0
#
# Computes the solution
#
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1] 
    sigmar , sigmat =ela.prering(x , y , a , b , pa , pb)
    SOL[i, 0] = sigmar
    SOL[i, 1] = sigmat
#
# Plot the solution
#
np.savetxt("usol.txt", SOL)
plo.plot_stress(SOL , nodes , elements , plt_type ="contourf",  levels = 12 )
#
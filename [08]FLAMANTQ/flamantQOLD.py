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
SOL = np.zeros([nn])
#
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
height = np.amax(coords[:,1])
#
# Define solution parameters
#
p = 1.0
#
# Computes the solution
#
for i in range(0,nn):
    X = coords[i,0]
    Y = coords[i,1]
    y = X
    x = Y - height 
    sigma =ela.flamantQ(x , y , p , 45.0)
    SOL[i] = sigma
#
# Plot the solution
#
plo.plot_UVAR(SOL, nodes , elements , plt_type ="contourf",  levels = 24 )
#
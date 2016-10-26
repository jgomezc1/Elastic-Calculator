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
U=np.zeros([nn , 2])
#
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
#
# Define solution parameters
#
P = -50.0
nu = 0.30
E = 1000.0
I = 42.67
L = 24.0
h = 8.0
#
# Computes the solution
#
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1]
# Call a user defined solution. 
    u, v, exx, eyy, gammaxy =ela.beam(x, y, nu, P, E, I, L, h)
    U[i , 0] = u
    U[i , 1] = v
#
# Plot the solution
#
plo.plot_disp(U, nodes, elements)
#
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
phid = 45.0
phi  = ela.radianes(phid)
l = np.sqrt(16.)
b = l*np.cos(phi)
h = l*np.sin(phi)
var = geo.wedge(l , phid, 0.1)
nodes , elements , nn =geo.create_model(var , False )
plo.viewmesh(nodes , elements , True)
coords=np.zeros([nn,2])
U=np.zeros([nn , 2])
Sig=np.zeros([nn , 2])
#
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
"""
Computes the solution
"""
nu = 1.0/3.0
E = 1.0
S = 1.0
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1]
    X = x+b
    Y = y-h
    ux , uy , sx , sy = ela.cunia(X , Y , phi , l , nu , E , S)
    U[i , 0] = ux
    U[i , 1] = uy
    Sig[i , 0] = sx
    Sig[i , 1] = sy
"""
Plot the solution
"""
plo.plot_disp(U, nodes, elements , 1 , plt_type="contourf", levels=12 , savefigs = True)
plo.plot_stress(Sig, nodes, elements , 2 , savefigs = True)
#

#
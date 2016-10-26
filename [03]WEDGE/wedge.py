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
phid = 39.
phi  = ela.radianes(phid)
l = np.sqrt(16.)
var = geo.wedge(l , phid, 0.1)
nodes , elements , nn =geo.create_model(var , False)
coords=np.zeros([nn,2])
U=np.zeros([nn , 2])
Sig=np.zeros([nn , 2])
#
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
"""
Computes the solution
"""
nu = 0.30
E = 1.0
S = 1.0
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1]
    ux , uy , sx , sy = ela.cunia(x , y , phi , l , nu , E , S)
    U[i , 0] = ux
    U[i , 1] = uy
    Sig[i , 0] = sx
    Sig[i , 1] = sy
"""
Plot the solution
"""
plo.plot_disp(U, nodes, elements)
plo.plot_stress(Sig, nodes, elements)
#
ux , uy , sx , sy =ela.cunia(0 , 0 , phi , l , nu , E , S)
sxy = 0
plo.viewmesh(nodes , elements , True)
#
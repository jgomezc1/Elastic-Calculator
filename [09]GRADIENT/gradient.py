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
(i)   Discretizes a rectangular domain with linear quads.
(ii)  Computes the displacement and strain field at the nodes of the mesh. (The displacement field
      corresponds to the elasticity solution for a cantelever beam).
(iii) Using the nodes and elements of the finite element mesh creates a triangulation object
      intended for later interpolation of the fields.
(iv)  Compares the analytical strain field with a displacement-based strain field.

"""
"""
Creates mesh files.
"""
L = 24.0
h = 24.0
ietype = 9
order  = 2
var = geo.beam(L, h, 0.2 , ietype)
geo.create_mesh(order , var )
nodes , elements , nn = geo.writefiles(ietype , var)
#
coords=np.zeros([nn,2])
U = np.zeros([nn , 2 ])
STR = np.zeros([nn , 3 ])
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
"""
Computes the analytic displacement and strain solution.
"""
P = -50.0
nu = 0.30
E = 1000.0
I = 42.67
L = 24.0
h = 8.0
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1]
    u, v, exx, eyy, gammaxy =ela.beam(x, y, nu, P, E, I, L, h)
    U[i , 0] = u
    U[i , 1] = v
    STR[i , 0]= exx
    STR[i , 1]= eyy
    STR[i , 2]= gammaxy
"""
Plot the analytic displacement and strain solution
"""
plo.plot_VFIELD(U  , nodes, elements , 1)
plo.plot_TFIELD(STR, nodes, elements , 1)
"""
Plot the displacement-based displacement gradient
"""
DuDx , DuDy = plo.plot_GRAD(U[: , 0] , nodes , elements , 1)
DvDx , DvDy = plo.plot_GRAD(U[: , 1] , nodes , elements , 1)
"""
Computes and plots the displacement-based shear strain.
"""
str = 0.5 * (DuDy + DvDx)
plo.plot_SFIELD(str  , nodes, elements , 1)
#
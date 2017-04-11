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
import interfaces as gui
import elasticity as ela
from sympy import init_printing
init_printing()
"""
Creates model.
"""
c , ietype , order =gui.mesh_gui()
r , l , h , ninc = gui.canyon_prs()


#ninc = 4097
#r = 1.0
#l = 6.0
#h = 3.0
#c = 0.15
#ietype = 2
#order  = 1
var = geo.canyon(r, l, h, c , ietype)
geo.create_mesh(order , var  , seemesh = True)
nodes , elements , nn = geo.writefiles(ietype , var)
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

# Plot the solution

#plo.plot_SFIELD(SOL[:,  0], nodes, elements , 1 , plt_type="contourf",  levels=12)


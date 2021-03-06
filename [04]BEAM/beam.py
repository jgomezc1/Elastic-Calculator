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
import interfaces as gui
"""
Creates mesh files.
"""
gui.beam_hlp()
c , ietype , order =gui.mesh_gui()
L , h , I , nu , E , P =gui.beam_prs()
var = geo.beam(L, h, c , ietype)
geo.create_mesh(order , var )
nodes , elements , nn = geo.writefiles(ietype , var)
#
coords=np.zeros([nn,2])
U=np.zeros([nn , 2])
STR = np.zeros([nn , 3 ])
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
plo.viewmesh(nodes , elements , True)
"""
Computes the solution
"""
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1]
    u, v, exx, eyy, gammaxy =ela.beam(x , y , nu , P , E , I , L , h)
    U[i , 0] = u
    U[i , 1] = v
    STR[i , 0]= exx
    STR[i , 1]= eyy
    STR[i , 2]= gammaxy
"""
Plot the solution
"""
plo.plot_disp(U  , nodes, elements, 1)
plo.plot_strain(STR , nodes , elements,1)
#
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
c , ietype , order =gui.mesh_gui()
phid , l , q = gui.flamantQ_prs()

phi  = ela.radianes(phid)
var = geo.wedge(l , phid, c , ietype)
geo.create_mesh(order , var  , seemesh = True)
nodes , elements , nn = geo.writefiles(ietype , var)
coords=np.zeros([nn,2])
SOL = np.zeros([nn])
#
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]

"""
Computes the solution
"""
q = 1.0
height = np.amax(coords[:,1])
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1]
    Y = x
    X = height-y
    sigma =ela.flamantQ(X , Y , q , phid)
    SOL[i] = sigma
"""
Plot the solution
"""
plo.plot_SFIELD(SOL, nodes , elements , 1 , plt_type ="contourf",  levels = 24 )
#
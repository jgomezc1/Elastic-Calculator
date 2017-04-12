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
import interfaces as gui
from sympy import init_printing
init_printing()
"""
Define the model and problem parameters
"""
gui.ring_hlp()
c , ietype , order =gui.mesh_gui()
a , b , pa , pb =gui.ring_prs()
var = geo.ring(a , b , c , ietype)
geo.create_mesh(order , var  , seemesh = True)
nodes , elements , nn = geo.writefiles(ietype , var)
"""
Define solution arrays
"""
coords=np.zeros([nn,2])
SOL = np.zeros([nn , 2])
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
"""
Computes the solution
"""
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1] 
    sigmar , sigmat =ela.prering(x , y , a , b , pa , pb)
    SOL[i, 0] = sigmar
    SOL[i, 1] = sigmat
"""
Plot the solution
"""
plo.plot_stress(SOL , nodes , elements , 1 , plt_type ="pcolor",  levels = 12 )
plo.viewmesh(nodes , elements , True)
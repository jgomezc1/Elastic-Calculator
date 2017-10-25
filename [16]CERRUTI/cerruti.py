# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:36:56 2015

@author: eafit
"""
#from sympy import init_printing
#init_printing()
import numpy as np
from os import sys
sys.path.append('../CALCULATOR/')
import elasticity as ela
import plotter as plo
import generategeo as geo
import interfaces as gui
"""
Creates mesh files.
"""
gui.boussi_hlp()
c , ietype , order =gui.mesh_gui()
l, h , P, nu , E  = gui.boussi_prs()
var = geo.boussinesq(l, h, c , ietype)
geo.create_mesh(order , var  )
nodes , elements , nn = geo.writefiles(ietype , var)
#
coords=np.zeros([nn,2])
SOLS = np.zeros([nn])
SOLU = np.zeros([nn , 2])
SOLC = np.zeros([nn , 3])
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
"""
Computes the solution
""" 
height = np.amax(coords[:,1])
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1]
    Y = - x
    X = height-y
    sigma = ela.cerrutipol(X , Y , P)

    SOLS[i] = sigma

#

"""
Plot the solution
"""
plo.plot_SFIELD(SOLS, nodes , elements , 1 , plt_type ="contourf", levels = 48 )
#plo.viewmesh(nodes , elements , True)
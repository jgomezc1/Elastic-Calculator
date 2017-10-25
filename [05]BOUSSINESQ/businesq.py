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
    sigma = ela.boussipol(X , Y , P)
    sx , sy , txy      = ela.boussicar(X , Y , P)
    ur , ut = ela.boussidispol(X , Y , P , E , nu , h)
    SOLS[i] = sigma
    SOLU[i , 0] = ur
    SOLU[i , 1] = ut 
#
    SOLC[i , 0] = sx
    SOLC[i , 1] = sy
    SOLC[i , 2] = txy
"""
Plot the solution
"""
plo.plot_SFIELD(SOLS, nodes , elements , 1 , plt_type ="contourf", levels = 48 )
plo.plot_disp(SOLU, nodes   , elements , 2 , plt_type="contourf" ,   levels = 12 )
plo.plot_TFIELD(SOLC, nodes , elements , 3 , plt_type="contourf" , levels = 24  )
#plo.viewmesh(nodes , elements , True)
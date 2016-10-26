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
l = 20.0
h = 20.0
var = geo.boussinesq(l, h, 1.0)
nodes , elements , nn =geo.create_model(var )
#
coords=np.zeros([nn,2])
SOLS = np.zeros([nn])
SOLU = np.zeros([nn , 2])
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
"""
Computes the solution
"""
p = 1.0
E = 1.0
enu = 0.3
 
height = np.amax(coords[:,1])
for i in range(0,nn):
    X = coords[i,0]
    Y = coords[i,1]
    y = X     #shifts the origin for l = 5.0
    x = Y - height 
    sigma =ela.boussi(x,y,p)
    ur , ut = ela.boussidis(x , y , p , E , enu , height)
    SOLS[i] = sigma
    SOLU[i , 0] = ur
    SOLU[i , 1] = ut    
"""
Plot the solution
"""
plo.plot_UVAR(SOLS, nodes , elements , plt_type ="contourf", levels = 12 )
plo.plot_disp(SOLU, nodes , elements , plt_type="contourf" , levels = 12 )
#
plo.viewmesh(nodes , elements)
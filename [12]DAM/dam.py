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
h = 9.0
ietype = 9
order  = 2
var = geo.dam(h , 0.25, ietype)
geo.create_mesh(order , var  , seemesh = True)
nodes , elements , nn = geo.writefiles(ietype , var)
plo.viewmesh(nodes , elements , True)
coords=np.zeros([nn,2])
Sig=np.zeros([nn , 3])
#
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
"""
Computes the solution
"""
gamma = 1.0/3.0

for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1]
    sx , sy , tao  = ela.dam(x , y , gamma)
    Sig[i , 0] = sx
    Sig[i , 1] = sy
    Sig[i , 2] = tao
"""
Plot the solution
"""
#
plo.plot_tension(Sig , nodes , elements, 1)
#
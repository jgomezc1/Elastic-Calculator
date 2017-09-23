# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 15:47:48 2017

@author: Carol
"""

from __future__ import division
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
Creando los archivos .msh
"""
gui.ellipse_hlp()
a , b , c , ietype , order, contornos =gui.ellipse()
var = geo.Ellipse(a , b , c , ietype);
geo.create_mesh(order , var  , seemesh = False)
nodes , elements , nn = geo.writefiles(ietype , var)
"""
Define solution arrays
"""
coords=np.zeros([nn,2])
SOL = np.zeros([nn]) 
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
"""
Computes the solution
"""
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1] 
    alabeo =ela.ellipse(a, b , x , y)
    SOL[i] = alabeo

"""
(iii) Plot the solution using the appropriate function from plotter.py
"""
plo.plot_SFIELD(SOL, nodes , elements, 1 , plt_type ="contourf", levels = contornos )
#
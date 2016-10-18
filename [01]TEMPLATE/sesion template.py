# -*- coding: utf-8 -*-
"""
Authors:
Juan Vergara.
Nicolas Guarin.
Juan Gomez.
Template for the elasticity solutions plotter. A user defined solution can be coded in 3 steps:
(i)   Define the model using basic shapes from the geometry generator modulde (generategeo.py) or
      create a new domain (see mygeom). In any case the model is represented by the nodes.txt and
      eles.txt files corresponding to a finite element mesh. These files can be specified directly
      in which case the functions defined in the module generategeo.py are not required.
(ii)  Code your own elasticity solution into the module elasticity.py. See ela.myfunction.
(iii) Plot the solution: use the module plotter.py to plot vector and tensor fields as required.
---------------------------------------------------------------------------------------------------------
In summary the program requires the following modules:

1. plotter.py    : This is the plotter perse.
2. elasticity.py : Module that contains the elasticity solution at a given point (x , y).
3. generatego.py : Module to create nodes.txt and eles.txt files using external meshing tools (GMESH and mesher.for)
---------------------------------------------------------------------------------------------------------
"""
import numpy as np
from os import sys
sys.path.append('../CALCULATOR/')
import elasticity as ela
import plotter as plo
import generategeo as geo
from sympy import init_printing
init_printing()
"""
(i)Creates model (Code your own function into the generategeo.py module).
"""
l = 1.5
h = 2.0
c = 0.5
var = geo.mygeom(l, h, c)
nodes , elements , nn =geo.create_model(var)
"""
Define solution arrays
"""
coords=np.zeros([nn,2])
SOL = np.zeros([nn]) # Modificar el arreglo SOL para graficar campos de diferente orden, e.g., vectores, tensores.
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
"""
(ii)Compute the solution after coding the user defined function myfunction().
Define as many parameters as required by the specific solution.
"""
par1 = 1.0
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1]
    uu =ela.myfunction(x,y,par1)
    SOL[i] = uu
"""
(iii) Plot the solution using the appropriate function from plotter.py
"""
plo.plot_UVAR(SOL, nodes , elements , plt_type ="contourf", levels = 12 )
#
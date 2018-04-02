# -*- coding: utf-8 -*-
"""
Authors:
Juan Gomez.
Nicolas Guarin.
Example for the elasticity solutions plotter. A user defined solution can be coded in 3 steps:
(i)   Define the model using basic shapes from the geometry generator modulde (generategeo.py) or
      create a new domain (see wedge). In any case the model is represented by the nodes.txt and
      eles.txt files corresponding to a finite element mesh. These files can be specified directly
      in which case the functions defined in the module generategeo.py are not required.
(ii)  Code your own elasticity solution into the module elasticity.py. See ela.cunia.
(iii) Plot the solution: use the module plotter.py to plot vector and tensor fields as required.
---------------------------------------------------------------------------------------------------------
In summary the program requires the following modules:

1. plotter.py     : This is the plotter perse.
2. elasticity.py  : Module that contains the elasticity solution at a given point (x , y).
3. generategeo.py : Module to create nodes.txt and eles.txt files using external meshing tools (Gmsh and meshio)
---------------------------------------------------------------------------------------------------------
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
(i)Creates the model (Code your own function into the generategeo.py module).
"""
gui.wedge_hlp()
c , ietype , order =gui.mesh_gui()
phid , l , nu , E , S = gui.wedge_prs()
phi  = ela.radianes(phid)
b = l*np.cos(phi)
h = l*np.sin(phi)

var = geo.wedge(l , phid, 0.1 , ietype)
geo.create_mesh(order , var )
nodes , elements , nn = geo.writefiles(ietype , var)
plo.viewmesh(nodes , elements , True)
coords=np.zeros([nn,2])
U=np.zeros([nn , 2])
Sig=np.zeros([nn , 2])
#
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
"""
(ii)Compute the solution after coding the user defined function cunia().
Define as many parameters as required by the specific solution.
"""
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1]
    X = x+b
    Y = y-h
    ux , uy , sx , sy = ela.cunia(X , Y , phi , l , nu , E , S)
    U[i , 0] = ux
    U[i , 1] = uy
    Sig[i , 0] = sx
    Sig[i , 1] = sy
"""
(iii) Plot the solution using the appropriate function from plotter.py
"""
plo.plot_disp(U, nodes, elements , 1 , plt_type="contourf", levels=12 , savefigs = True)
plo.plot_stress(Sig, nodes, elements , 2 , savefigs = True)
#

#
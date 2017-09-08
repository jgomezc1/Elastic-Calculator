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
3. generategeo.py : Module to create nodes.txt and eles.txt files using external meshing tools (GMESH and mesher.for)
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
try:
    import easygui
    msg = "Solution plotter template"
    title = "Enter the problem parameters"
    fieldNames = ["Length","Width","Element size","Element type","Intrpolation order"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = easygui.multenterbox(msg,title, fieldNames)
    

    l = float(fieldValues[0])
    h = float(fieldValues[1])
    c = float(fieldValues[2])
    ietype = int(fieldValues[3])
    order = int(fieldValues[4])
except:
    a1 = raw_input("Length")
    b1 = raw_input("Width")
    c1 = raw_input("Element size")
    ietype1 = raw_input("Element type")
    order1 = raw_input("Interpolation order")
    l = float(a1)
    h = float(b1)
    c = float(c1)
    ietype = int(ietype1)
    order = int(order1)
var = geo.mygeom(l, h, c , ietype)
geo.create_mesh(order , var  , seemesh = True)
nodes , elements , nn = geo.writefiles(ietype , var)
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
plo.plot_SFIELD(SOL, nodes , elements, 1 , plt_type ="contourf", levels = 12 )
#













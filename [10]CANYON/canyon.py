# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:36:56 2015

@author: eafit
"""
import numpy as np
from os import sys
sys.path.append('../CALCULATOR/')
import plotter as plo
import generategeo as geo
import elasticity as ela
from sympy import init_printing
init_printing()
"""
Creates model.
"""
try:
    import easygui
    msg = "Semi-circular canyon under SH waves"
    title = "Enter the problem parameters"
    fieldNames = ["Radius","Side length","Height","Element size","Element type","Intrpolation order"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = easygui.multenterbox(msg,title, fieldNames)
    

    r = float(fieldValues[0])
    l = float(fieldValues[1])
    h = float(fieldValues[2])
    c = float(fieldValues[3])
    ietype = int(fieldValues[4])
    order = int(fieldValues[5])
except:
    a1 = raw_input("Radius")
    b1 = raw_input("Side length")
    c1 = raw_input("Hight")
    d1 = raw_input("Element size")
    ietype1 = raw_input("Element type")
    order1 = raw_input("Interpolation order")
    r = float(a1)
    l = float(b1)
    h = float(c1)
    c = float(d1)
    ietype = int(ietype1)
    order = int(order1)

ninc = 4097
#r = 1.0
#l = 6.0
#h = 3.0
#c = 0.15
#ietype = 2
#order  = 1
var = geo.canyon(r, l, h, c , ietype)
geo.create_mesh(order , var  , seemesh = True)
nodes , elements , nn = geo.writefiles(ietype , var)
plo.viewmesh(nodes , elements , True)
"""
Define solution arrays
"""
coords=np.zeros([nn,2])
SOL = np.zeros([nn,ninc])
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
"""
Computes the solution
"""
for i in range(nn):
    x = coords[i,0]
    y = coords[i,1]
    u = ela.trifunac(x , y )
    for j in range(ninc):
        SOL[i,j] = u[j]

# Plot the solution

#plo.plot_SFIELD(SOL[:,  0], nodes, elements , 1 , plt_type="contourf",  levels=12)


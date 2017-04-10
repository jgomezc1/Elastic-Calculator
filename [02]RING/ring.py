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
from sympy import init_printing
init_printing()

try:
    import easygui
    msg = "Cylinder under internal pressure"
    title = "Enter the problem parameters"
    fieldNames = ["Internal radius","External radius","Element size","Element type","Intrpolation order"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = easygui.multenterbox(msg,title, fieldNames)
    

    a = float(fieldValues[0])
    b = float(fieldValues[1])
    c = float(fieldValues[2])
    ietype = int(fieldValues[3])
    order = int(fieldValues[4])
except:
    a1 = raw_input("Internal radius")
    b1 = raw_input("Eternal radius")
    c1 = raw_input("Element size")
    ietype1 = raw_input("Element type")
    order1 = raw_input("Interpolation order")
    a = float(a1)
    b = float(b1)
    c = float(c1)
    ietype = int(ietype1)
    order = int(order1)

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
Define pressures (a: internal; b external)
"""
pa =  1.0
pb =  2.0
"""
Computes the solution
"""
for i in range(0,nn):
    x = coords[i,0]
    y = coords[i,1] 
    sigmar , sigmat =ela.prering(x , y , a , b , pa , pb)
    SOL[i, 0] = sigmar
    SOL[i, 1] = sigmat
#
# Plot the solution
#
plo.plot_stress(SOL , nodes , elements , 1 , plt_type ="pcolor",  levels = 12 )
plo.viewmesh(nodes , elements , True)
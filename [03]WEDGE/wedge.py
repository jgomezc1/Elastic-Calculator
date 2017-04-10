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
try:
    import easygui
    msg = "Self equilibrated wedge"
    title = "Enter the problem parameters"
    fieldNames = ["Semi-angle (Degrees)","Length","Element size","Element type","Intrpolation order"]
    fieldValues = []  
    fieldValues = easygui.multenterbox(msg,title, fieldNames)
    

    phid = float(fieldValues[0])
    l = float(fieldValues[1])
    c = float(fieldValues[2])
    ietype = int(fieldValues[3])
    order = int(fieldValues[4])
except:
    a1 = raw_input("Semi-angle")
    b1 = raw_input("Length")
    c1 = raw_input("Element size")
    ietype1 = raw_input("Element type")
    order1 = raw_input("Interpolation order")
    phid = float(a1)
    l = float(b1)
    c = float(c1)
    ietype = int(ietype1)
    order = int(order1)

phi  = ela.radianes(phid)
b = l*np.cos(phi)
h = l*np.sin(phi)

var = geo.wedge(l , phid, 0.1 , ietype)
geo.create_mesh(order , var  , seemesh = True)
nodes , elements , nn = geo.writefiles(ietype , var)
plo.viewmesh(nodes , elements , True)
coords=np.zeros([nn,2])
U=np.zeros([nn , 2])
Sig=np.zeros([nn , 2])
#
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
"""
Computes the solution
"""
nu = 1.0/3.0
E = 1.0
S = 1.0
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
Plot the solution
"""
plo.plot_disp(U, nodes, elements , 1 , plt_type="contourf", levels=12 , savefigs = True)
plo.plot_stress(Sig, nodes, elements , 2 , savefigs = True)
#

#
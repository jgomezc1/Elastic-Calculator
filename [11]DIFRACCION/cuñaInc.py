# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:22:21 2017

#@author: JULIAN PARRA
#"""

import numpy as np
from os import sys
sys.path.append('../CALCULATOR/')
from sympy import init_printing
init_printing()
import elasticity as ela
import plotter as plo
import generategeo as geo

ninc = 4097

L1 = 20
theta = 90
c = 1.2
var = geo.WedgeDifrac(L1,theta,c)
nodes , elements , nn = geo.create_model(var , False)
plo.viewmesh(nodes , elements , True)

"""
Define solution arrays
"""
#nodes = np.loadtxt("nodes.txt")
#elements = np.loadtxt("nodes.txt")
#
#
coords=np.zeros([nn,2])
SOL = np.zeros([nn,ninc])
coords[:,0]=nodes[:,1]
coords[:,1]=nodes[:,2]
#
"""
Computes the solution
"""
#
for i in range(nn):
    x = coords[i,0]*-1
    y = coords[i,1]-L1*np.cos(theta*np.pi/360)
    u = ela.DifractionSesma(x,y)
    for j in range(ninc):
        SOL[i,j] = u[j]

#Plot the solution
#
#plo.plot_SFIELD(SOL[:,2000], nodes, elements , 1 , plt_type="contourf",  levels=12)

#


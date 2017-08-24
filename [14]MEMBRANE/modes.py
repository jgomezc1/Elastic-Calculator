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
import interfaces as gui
import elasticity as ela
from sympy import init_printing
init_printing()
"""
Creates model.
"""
gui.box_hlp()
c , ietype , order =gui.mesh_gui()
l , h , ninc , Tt = gui.membrane_prs()
dt = Tt / ninc
N = 10
M = 10
var = geo.quad(l, h, c , ietype)
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
    x = coords[i,0] + h/2.0
    y = coords[i,1]
    u = ela.modeplotter(x, y , l , h , 3 , 1 , ninc , dt )
    for j in range(ninc):
        SOL[i,j] = u[j]

ne = len(elements)
plo.vtk_maker_4noded(nodes , elements , SOL , nn , ne , ninc , 1 )
#
#umod = np.zeros([nn ])
#for i in range(nn):
#    x = coords[i,0]
#    y = coords[i,1]
#    uu = ela.modplotter(x, y , l , h , 3 , 3  )
#    umod[i] = uu
#plo.plot_SFIELD(umod, nodes, elements, 1  , plt_type="contourf",  levels=12,savefigs = True)


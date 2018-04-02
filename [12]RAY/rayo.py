# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:36:56 2015

@author: eafit
"""
import numpy as np
from os import sys
sys.path.append('../CALCULATOR/')
import plotter as plo
import matplotlib.pyplot as plt
import signals as sig
import generategeo as geo
import interfaces as gui
import elasticity as ela
from sympy import init_printing
init_printing()

def verification(ninc , dt , fs):
    plt.figure(0)
    DATOS = np.loadtxt('respuesta.txt' )
    signal=np.zeros([ninc , 71], dtype=float)
    k = 0
    for j in range(5 , 100):
        for i in range(ninc):
            signal[i , k ] =  DATOS[j , i] + k/5
        sig.grafsignalG(signal[: , k] , 'salida' , 'Displacement' , 'l' , 0.0 , 20.0 , dt , 0)
        k = k+1
    return


"""
Creates model.
"""
gui.box_hlp()
c , ietype , order =gui.mesh_gui()
l , h , Gamma , beta , Tt , Tc , fc = gui.quad_prs()
var = geo.quad(l, h, c , ietype)
geo.create_mesh(order , var  )
nodes , elements , nn = geo.writefiles(ietype , var)
plo.viewmesh(nodes , elements , True)
"""
Define solution arrays
"""
dt = 1.0/(8.0*fc)
ninc = int(Tt/dt)
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
    u = ela.single_ray(x , y , Gamma , beta , Tt , Tc , fc )
    for j in range(ninc):
        SOL[i,j] = u[j]

ne = len(elements)
plo.vtk_maker_4noded(nodes , elements , SOL , nn , ne , ninc , 1 )
np.savetxt('respuesta.txt' , SOL )
verification(ninc , dt , 10.0)

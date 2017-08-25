# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:36:56 2015

@author: eafit
"""
from __future__ import division
from os import sys
sys.path.append('../CALCULATOR/')
import numpy as np
from numpy import sin, cos, sqrt, pi
import plotter as plo


def rect_grid(length, height, nx, ny, eletype=None):
    """Generate a structured mesh for a rectangle
    The coordinates of the nodes will be defined in the
    domain [-length/2, length/2] x [-height/2, height/2].
    Parameters
    ----------
        length : float
            Length of the domain.
        height : gloat
            Height of the domain.
        nx : int
            Number of points in the x direction.
        ny : int
            Number of points in the y direction.
        eletype : None
            It does nothing right now.
    Returns
    -------
        x : ndarray (float)
            x-coordinates for the nodes.
        y : ndarray (float)
            y-coordinates for the nodes.
        els : ndarray
            Array with element data.
    """
    y, x = np.mgrid[-height/2:height/2:ny*1j,
                    -length/2:length/2:nx*1j]
    els = np.zeros(((nx - 1)*(ny - 1), 7), dtype=int)
    els[:, 1] = 1
    for row in range(ny - 1):
        for col in range(nx - 1):
            cont = row*(nx - 1) + col
            els[cont, 0] = cont
            els[cont, 3:7] = [cont + row, cont + row + 1,
                              cont + row + nx + 1, cont + row + nx]
    return x.flatten(), y.flatten(), els


def membrane_instant(x, y, t, Nx, Ny):
    z = np.zeros_like(x)
    for m in range(1, Nx + 1, 2):
        for n in range(1, Ny + 1, 2):
            k = sqrt(m**2 + 4*n**2)
            z += sin(m*pi*x) * sin(2*n*pi*y)*cos(20*pi*k*t)/(m*n)**3

    return 0.64*z/pi**6


Nx = 10
Ny = 10
nx = 100
ny = 100
nt = 100
length = 1.0
height = 0.5
dt = 0.001
x, y, els = rect_grid(length, height, nx, ny)
x += length/2
y += height/2
nnodes = x.shape[0]
nodes = np.column_stack((range(nnodes), x, y))
solution = np.zeros((x.shape[0], nt))
for cont in range(nt):
    t = dt * cont
    solution[:, cont] = membrane_instant(x, y, t, Nx, Ny)


nels = len(els)
plo.vtk_maker_4noded(nodes, els, solution, nnodes, nels, nt, 1)

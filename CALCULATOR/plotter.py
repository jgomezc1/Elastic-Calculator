# -*- coding: utf-8 -*-
"""
Este modulo contiene rutinas de graficacion de campos de desplazamiento,
de variables de usuario (escalares) y de tensiones usando traiangulacion.
Rutinas adicionales basadas en estas pueden adicionarse.
"""
from __future__ import division
import numpy as np
#import femutil as fe
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
#from scipy.interpolate import griddata, interp2d
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 14
rcParams['image.cmap'] = "YlGnBu_r"
#
def plot_disp(UC, nodes, elements, plt_type="contourf", levels=12,
               savefigs=False, title="Solution:"):
    """Plot the nodal displacement using a triangulation

    Parameters
    ----------
    UC : ndarray (float)
      Array with the displacements.
    nodes : ndarray (float)
      Array with number and nodes coordinates:
        `number coordX coordY BCX BCY`
    elements : ndarray (int)
      Array with the node number for the nodes that correspond to each
      element.

    """
    tri = mesh2tri(nodes, elements)
    tri_plot(tri, UC[:, 0], title=r'$u_x$',
             figtitle=title + "Horizontal displacement",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="ux_sol.pdf")
    tri_plot(tri, UC[:, 1], title=r'$u_y$',
             figtitle=title + "Vertical displacement",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="uy_sol.pdf")
#
def plot_UVAR(UC, nodes, elements, plt_type="contourf",  levels=12,
               savefigs=False, title="Solution:"  ):
    """Plot the a scalar user defined field using a triangulation

    Parameters
    ----------
    UC : ndarray (float)
      Array with the displacements.
    nodes : ndarray (float)
      Array with number and nodes coordinates:
        `number coordX coordY`
    elements : ndarray (int)
      Array with the node number for the nodes that correspond to each
      element.

    """
    tri = mesh2tri(nodes, elements)
    tri_plot(tri, UC , title=r'$U_{var}$',
             figtitle=title + "User variable",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="uservar.pdf")        
#
def plot_stress(S_nodes, nodes, elements, plt_type="contourf", levels=12,
               savefigs=False):
    """Plot a 2 component stresses field using a triangulation
    
    The stresses need to be computed at nodes first.

    Parameters
    ----------
    S_nodes : ndarray (float)
      Array with the nodal stresses.
    nodes : ndarray (float)
      Array with number and nodes coordinates:
        `number coordX coordY`
    elements : ndarray (int)
      Array with the node number for the nodes that correspond to each
      element.

    """
    tri = mesh2tri(nodes, elements)
    tri_plot(tri, S_nodes[:, 0], title=r'$\sigma_{11}$',
             figtitle="Solution: sigma-xx stress",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="sigmaxx_sol.pdf")
    tri_plot(tri, S_nodes[:, 1], title=r'$\sigma_{22}$',
             figtitle="Solution: sigma-xy stress",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="sigmaxy_sol.pdf")             
#

def mesh2tri(nodes, elements):
    """Generate a  matplotlib.tri.Triangulation object from the mesh
    
    Parameters
    ----------
    nodes : ndarray (float)
      Array with number and nodes coordinates:
        `number coordX coordY BCX BCY`
    elements : ndarray (int)
      Array with the node number for the nodes that correspond to each
      element.
    
    Returns
    -------
    tri : Triangulation
        An unstructured triangular grid consisting of npoints points
        and ntri triangles.
    
    """
    x = nodes[:, 1]
    y = nodes[:, 2]
    triangs = []
    for el in elements:
        if el[1]==1:
            triangs.append(el[[3, 4, 5]])
            triangs.append(el[[5, 6, 3]])
        if el[1]==2:
            triangs.append(el[[3, 6, 8]])
            triangs.append(el[[6, 7, 8]])
            triangs.append(el[[6, 4, 7]])
            triangs.append(el[[7, 5, 8]])
        if el[1]==3:
            triangs.append(el[3:])
    
    tri = Triangulation(x, y, np.array(triangs))
    return tri    


def tri_plot(tri, field, title="", figtitle="", levels=12, savefigs=False,
             plt_type="contourf" , filename="solution_plot.pdf" ):
    
    if plt_type=="pcolor":
        disp_plot = plt.tripcolor
    elif plt_type=="contourf":
        disp_plot = plt.tricontourf

    plt.figure(figtitle)
    disp_plot(tri, field, levels, shading="gouraud")
    plt.title(title)
    plt.colorbar(orientation='vertical')
    plt.axis("image")
    plt.grid()
    if savefigs:
        plt.savefig(filename)
#
def mohr(sxx , syy , sxy , nfig):
    """Plot Mohr circle for a 2D tensor"""
#    S11 = S[0][0] 
#    S12 = S[0][1] 
#    S22 = S[1][1]
    S11 = sxx 
    S12 = sxy 
    S22 = syy
    center = [(S11 + S22)/2.0, 0.0]
    radius = np.sqrt((S11 - S22)**2/4.0 + S12**2)
    Smin = center[0] - radius
    Smax = center[0] + radius
    
    
    print "Minimum Normal Stress: ", np.round(Smin,6)
    print "Maximum Normal Stress: ", np.round(Smax, 6)
    print "Average Normal Stress: ", np.round(center[0], 6)
    print "Minimum Shear Stress: ", np.round(-radius, 6)
    print "Maximum Shear Stress: ", np.round(radius, 6)
    plt.figure(nfig)
    circ = plt.Circle((center[0],0), radius, facecolor='#cce885', lw=3,
    edgecolor='#5c8037') 
    plt.axis('image')
    ax = plt.gca() 
    ax.add_artist(circ)
    ax.set_xlim(Smin - .1*radius, Smax + .1*radius)
    ax.set_ylim(-1.1*radius, 1.1*radius)
    plt.plot([S22, S11], [S12, -S12], 'ko')
    plt.plot([S22, S11], [S12, -S12], 'k')
    plt.plot(center[0], center[1], 'o', mfc='w')
    plt.text(S22 + 0.1*radius, S12, 'B')
    plt.text(S11 + 0.1*radius, -S12, 'A')
    plt.xlabel(r"$\sigma$", size=18)
    plt.ylabel(r"$\tau$", size=18)   
#    plt.show()        
#
#%%
if __name__ == "__main__":
    import doctest
    doctest.testmod()
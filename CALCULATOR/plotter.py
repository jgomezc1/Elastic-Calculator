# -*- coding: utf-8 -*-
"""
This module contains plotting functions for both, user defined and pre-defined
scalar, vector and tensor fields using triangulation.
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation, CubicTriInterpolator
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 14
rcParams['image.cmap'] = "YlGnBu_r"
#
def plot_disp(UC, nodes, elements, Ngra , plt_type="contourf", levels=12,
               savefigs=False, title="Solution:" ):
    """Plots a 2D nodal displacement field using a triangulation.

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
    tri_plot(tri, UC[:, 0] , Ngra, title=r'$u_x$',
             figtitle=title + "Horizontal displacement",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="ux_sol.pdf" )
    tri_plot(tri, UC[:, 1],  Ngra , title=r'$u_y$',
             figtitle=title + "Vertical displacement",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="uy_sol.pdf")


def plot_SFIELD(UC, nodes, elements, Ngra, plt_type="contourf",  levels=12,
               savefigs=False, title="Solution:"  ):
    """Plots a user defined scalar field using a triangulation.

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
    tri_plot(tri, UC , Ngra , title=r'$U_{var}$',
             figtitle=title + "User variable",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="uservar.pdf")


def plot_VFIELD(UC, nodes, elements, Ngra, plt_type="contourf",  levels=12,
               savefigs=False, title="Solution:" ):
    """Plots a 2D user defined vector field using a triangulation.

    Parameters
    ----------
    UC : ndarray (float)
      Array with the vector field.
    nodes : ndarray (float)
      Array with number and nodes coordinates:
        `number coordX coordY`
    elements : ndarray (int)
      Array with the node number for the nodes that correspond to each
      element.

    """
    tri = mesh2tri(nodes, elements)
    tri_plot(tri, UC[:, 0], Ngra , title=r'$u_x$',
             figtitle=title + "Horizontal component",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="ux_sol.pdf")
    tri_plot(tri, UC[:, 1], Ngra , title=r'$u_y$',
             figtitle=title + "Vertical component",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="uy_sol.pdf")


def plot_TFIELD(UC, nodes, elements, Ngra , plt_type="contourf",  levels=12,
               savefigs=False, title="Solution:" ):
    """Plots a 2D user defined symmetric tensor field using a triangulation.

    Parameters
    ----------
    UC : ndarray (float)
      Array with the vector field.
    nodes : ndarray (float)
      Array with number and nodes coordinates:
        `number coordX coordY`
    elements : ndarray (int)
      Array with the node number for the nodes that correspond to each
      element.

    """
    tri = mesh2tri(nodes, elements)
    tri_plot(tri, UC[:, 0], Ngra , title=r'$S_{xx}$',
             figtitle=title + "xx component",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="ux_sol.pdf")
    tri_plot(tri, UC[:, 1], Ngra , title=r'$S_{yy}$',
             figtitle=title + "yy component",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="uy_sol.pdf")
    tri_plot(tri, UC[:, 2], Ngra , title=r'$S_{xy}$',
             figtitle=title + "xy component",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="uxy_sol.pdf")


def plot_stress(S_nodes, nodes, elements, Ngra ,  plt_type="contourf", levels=12,
               savefigs=False ):
    """Plots a 2 component stresses field using a triangulation.

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
    tri_plot(tri, S_nodes[:, 0], Ngra ,  title=r'$\sigma_{11}$',
             figtitle="Solution: sigma-xx stress",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="sigmaxx_sol.pdf")
    tri_plot(tri, S_nodes[:, 1], Ngra ,  title=r'$\sigma_{22}$',
             figtitle="Solution: sigma-xy stress",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="sigmaxy_sol.pdf")


def plot_tension(e_nodes, nodes, elements, Ngra ,  plt_type="contourf", levels=12,
               savefigs=False):
    """Plots a 2 component stresses field using a triangulation.

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
    tri_plot(tri, e_nodes[:, 0], Ngra ,  title=r'$\sigma _{xx}$',
             figtitle="Solution: epsilon-xx strain",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="sigmaxx_sol.pdf")
    tri_plot(tri, e_nodes[:, 1], Ngra,  title=r'$\sigma _{yy}$',
             figtitle="Solution: epsilon-yy strain",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="sigmayy_sol.pdf")
    tri_plot(tri, e_nodes[:, 2], Ngra,  title=r'$sigma _{xy}$',
             figtitle="Solution: gamma-xy strain",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="sigmaxy_sol.pdf")


def plot_strain(e_nodes, nodes, elements, Ngra ,  plt_type="contourf", levels=12,
               savefigs=False):
    """Plots a 2 component stresses field using a triangulation.

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
    tri_plot(tri, e_nodes[:, 0], Ngra ,  title=r'$\varepsilon _{xx}$',
             figtitle="Solution: epsilon-xx strain",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="sigmaxx_sol.pdf")
    tri_plot(tri, e_nodes[:, 1], Ngra,  title=r'$\varepsilon _{yy}$',
             figtitle="Solution: epsilon-yy strain",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="sigmaxy_sol.pdf")
    tri_plot(tri, e_nodes[:, 2], Ngra,  title=r'$\gamma_{xy}$',
             figtitle="Solution: gamma-xy strain",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="sigmaxy_sol.pdf")


def plot_GRAD(UC, nodes, elements, Ngra , plt_type="contourf",  levels=12,
               savefigs=False, title="Solution:" ):
    """Plots the gradient of a user defined scalar field using triangulation.

    Parameters
    ----------
    UC : ndarray (float)
      Array with the scalar field.
    nodes : ndarray (float)
      Array with number and nodes coordinates:
        `number coordX coordY`
    elements : ndarray (int)
      Array with the node number for the nodes that correspond to each
      element.

    """
    tri = mesh2tri(nodes, elements)
    tcu = CubicTriInterpolator(tri, UC)
    (DuDx, DuDy) = tcu.gradient(tri.x, tri.y)
    tri_plot(tri, DuDx, Ngra , title=r'$\frac{{\partial }}{{\partial x}}$',
             figtitle="x gradient",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="dudx.pdf")
    tri_plot(tri, DuDy, Ngra , title=r'$\frac{{\partial }}{{\partial y}}$',
             figtitle="y gradient",
             levels=levels, plt_type=plt_type, savefigs=savefigs,
             filename="dudy.pdf")
    return DuDx , DuDy


def mesh2tri(nodes, elements):
    """Generates a matplotlib.tri.Triangulation object from the mesh

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
        if el[1]==3:
            triangs.append(el[[3, 4, 5]])
            triangs.append(el[[5, 6, 3]])
        if el[1]==9:
            triangs.append(el[[3, 6, 8]])
            triangs.append(el[[6, 7, 8]])
            triangs.append(el[[6, 4, 7]])
            triangs.append(el[[7, 5, 8]])
        if el[1]==2:
            triangs.append(el[3:])

    tri = Triangulation(x, y, np.array(triangs))
#
    return tri


def tri_plot(tri, field, Ngra ,  title="", figtitle="", levels=12, savefigs=False,
             plt_type="contourf" , filename="solution_plot.pdf"  ):

    plt.figure(Ngra)
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
def viewmesh(nodes , elements , view = False):
    #
    """Generates and displays a matplotlib.tri.Triangulation object created from a
       user defined finite element mesh given by nodes and elements.

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
        if el[1]==3:
            triangs.append(el[[3, 4, 5]])
            triangs.append(el[[5, 6, 3]])
        if el[1]==9:
            triangs.append(el[[3, 6, 8]])
            triangs.append(el[[6, 7, 8]])
            triangs.append(el[[6, 4, 7]])
            triangs.append(el[[7, 5, 8]])
        if el[1]==2:
            triangs.append(el[3:])

    tri = Triangulation(x, y, np.array(triangs))
#
    if view:
        plt.figure()
        plt.gca().set_aspect('equal')
        plt.triplot(tri, lw=0.5, color='red')

    return tri
#
def mohr(sxx , syy , sxy , nfig):
    """Plots Mohr circle for a 2D tensor"""
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


    print("Minimum Normal Stress: ", np.round(Smin,6))
    print("Maximum Normal Stress: ", np.round(Smax, 6))
    print("Average Normal Stress: ", np.round(center[0], 6))
    print("Minimum Shear Stress: ", np.round(-radius, 6))
    print("Maximum Shear Stress: ", np.round(radius, 6))
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

def vtk_maker_4noded(nodes , eles , SOL , nnodes , ne , ninc , vtinc ):
    """
     Author: Juan Fernando Zapata
     Writes VTK files for visualization with paraview
    """

    z = np.zeros((nnodes))
    y = np.zeros((nnodes))
    x = np.zeros((nnodes))
    npore = np.zeros(ne) # npore = número de nodos por elemento
    np.savetxt('VTK.txt', SOL, fmt='%f')
    SOL = np.loadtxt('VTK.txt')
    for i in range(ne):
        npore[i] = int(4)
    for j in range(0, ninc , vtinc):
        ind = str(j)
        H =  open('wave'+ ind + '.vtk', 'w')
        H.write("# vtk DataFile Version 3.1 \n")
        H.write("Canion de trifunac\n")
        H.write("ASCII \n")
        H.write("DATASET UNSTRUCTURED_GRID \n")
        H.write("POINTS              %i float" %(nnodes))
        H.write("\n")

        for i in range(nnodes):
            H.write(" %f  %f  %f " % (nodes[i,1], nodes[i,2], z[i]))
            H.write("\n")

        H.write("\n")
        H.write("CELLS              %i              %i" %(ne, 5*ne))
        H.write("\n")

        for i in range(ne):
            H.write(" %i  %i  %i  %i  %i " % (npore[i], eles[i,3], eles[i,4], eles[i,5], eles[i,6]))
            H.write("\n")

        H.write("\n")
        H.write("CELL_TYPES %i" %(ne))
        H.write("\n")

        for i in range(ne):
#            H.write(" %i " % (eles[i,2]))
            H.write(" %i " % (10))
            H.write("\n")

        H.write("\n")
        H.write("POINT_DATA              %i" %(nnodes))
        H.write("\n")
        H.write("VECTORS DISPLACEMENT float \n")

        for i in range(nnodes):
            H.write(" %f  %f  %f " % (x[i], y[i], SOL[i,j]))
            H.write("\n")

        H.write("\n")


    return

#%%
if __name__ == "__main__":
    import doctest
    doctest.testmod()
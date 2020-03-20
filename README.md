# Elastic-Calculator


![Displacement field in a wrench.](./CALCULATOR/img/wrench.png)

The Repo contains tools to visualized closed-form solutions over 2D-computational domains discretized into finite elements.

## Features
The Elastic-Calculator allows the visualization of closed-form solutions (e.g., elasticity theory solutions) using finite element meshes. It has been  created for academic purposes and it is part of the teaching material developed for the courses **IC0602 Introduction to the Finite Element Methods** , **IC0285 Computational Modeling** and **Continuous Mechanics** at Universidad EAFIT.

## How it works
In order to visualize a solution (available within this Repo) the user must execute the script for the problem of interest selected from the provided data-base. Each subroutine is identified with a number and the name of the solution, for instance [02]RING refers to the solution for a ring under pressure. Once the problem parameters are defined the script will create a finite element mesh using [Gmsh](http://gmsh.info/) (the free three-dimensional finite element mesh generator) in the background. The closed-form solution, coded in the python module elasticity.py (available in the folder CALCULATOR), is then evaluated at the nodes of the finite element mesh. To provide visualizations of the solution the mesh is triangulated by the post-processing module **plotter.py**. The triangulation is directly used by Python to produce an interpolated image using the nodal fields.

User provided solutions, different from the ones contained in the repo can also be implemented by adding the specific function to the module **elasticity.py** using a template like the one below.

```python
def myfunction(x, y, p):
    """
    Template for user defined elasticity solution.
    """
    ux=(x**2.+y**2.)**p
#    ux= -x-y
    return ux
```
Once the subroutine is added to the the file **elasticity.py** it can be invoked from the evaluation script as described in the folder [01]TEMPLATE and described here as follows:

```python
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
    a1 = input("Length")
    b1 = input("Width")
    c1 = input("Element size")
    ietype1 = input("Element type")
    order1 = input("Interpolation order")
    l = float(a1)
    h = float(b1)
    c = float(c1)
    ietype = int(ietype1)
    order = int(order1)
var = geo.mygeom(l, h, c , ietype)
geo.create_mesh(order , var )
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
```

The _repo_ is organized as follows:

1. `[xx]SOLUTION_NAME` Several folders with python scripts corresponding to existing solutions and ready to be tested.
2. `CALCULATOR` This is the main folder in the Repo as it stores the solution per se and other usefull tools lik: 

    - `elasticity.py`: The main program data base of solutions in the form of python functions.
    - `plotter.py`   : Subroutines for visualization of solution given a finite element mesh.
    - `generategeo.py`: gmsh templates for different pre-defined geometries.
    - `interafces.py`: Graphical input of solution parameters.
    - `signals.py`: Subroutins useful for processing time-domain solutions (see [10] CANYON)

## Instalation
The code is written in Python and it depends on numpy and matplotlib. The finite elment meshes created with **gmesh** are processed with [`meshio`](https://github.com/nschloe/meshio). In order to run the problems with a simple GUI the user needs to install [`easygui`](http://easygui.readthedocs.org/en/master/).  Both modules can be installed with:

    pip install easygui
    pip install meshio

To execute **gmesh** directly from within the CALCULATOR you must modify the file config.yml available in the folder CALCULATOR and indicate the PATH to the **gmesh** executable (see the current available version for an example).

## Authors
- [Juan Gomez](http://www.eafit.edu.co/docentes-investigadores/Paginas/juan-gomez.aspx), Professor at Universidad EAFIT.
- [Nicolás Guarín-Zapata](https://github.com/nicoguaro), Researcher at Universidad EAFIT.

## Instructions

The code is written in Python 2 dialect (we believe that it will work in Python 3 but we have not tested yet) and it depends on numpy, scipy and sympy. To use it clone the repo with

    git clone https://github.com/jgomezc1/FEM_PYTHON.git
   
uncompress the zip folder an run the main file in the Python console of your
preference.

## License

This project is licensed under the MIT license. The documents are licensed under Creative Commons Attribution License.

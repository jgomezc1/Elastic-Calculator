# Elastic-Calculator
![Scattering of SH waves.](./docs/img/trifunac.gif)

The Repo contains tools to visualized closed-form solutions over 2D-computational domains discretized into finite elements.

## Features
The Elastic-Calculator allows the visualization of closed-form solutions (e.g., elasticity theory solutions) using finite element meshes. It has been  created for academic purposes and it is part of the teaching material developed for the courses IC0602 Introduction to the Finite Element Methods and IC0285 Computational Modeling at Universidad EAFIT.

In order to visualize a solution (available within this Repo) the user must execute the script for the problem of interest selected from the provided data-base. Once the problem parameters are defined the script will create a finite element mesh using [Gmsh](http://gmsh.info/) (the free three-dimensional finite element mesh generator) in the background. The closed-form solution, coded in the python module elasticity.py, is then evaluated at the nodes of the finite element assemblage. In order to provide images of the solution the mesh is triangulated by the post-processing module plotter.py. The triangulation is directly used by Python to produce an intrpolated image using the nodal fields. User provided solutions, different from the ones contained in the repo can also be implemented by adding the specific function to the module elasticity.py.

The _repo_ is organized as follows:

1. `[xx]SOLUTION_NAME` Several folders with python scripts corresponding to existing solutions and ready to be tested.
2. `CALCULATOR` This is the main folder in the Repo as it stores the solution per se and other usefull tools lik: 

    - `elasticity.py`: The main program data base of solutions in the form of python functions.
    - `plotter.py`   : Subroutines for visualization of solution given a finite element mesh.
    - `generategeo.py`: gmsh templates for different pre-defined geometries.
    - `interafces.py`: Graphical input of solution parameters.
    - `signals.py`: Subroutins useful for processing time-domain solutions (see [10] CANYON)

## Instalation
The code is written in Python and it depends on numpy and matplotlib. The Gmesh, finite elment meshes are processed with [`meshio`](https://github.com/nschloe/meshio). On the other hand in order to run the problems with the GUI the user needs to install [`easygui`](http://easygui.readthedocs.org/en/master/).  Both modules can be installed with:

    pip install easygui
    pip install meshio

## Authors
- [Juan Gomez](http://www.eafit.edu.co/docentes-investigadores/Paginas/juan-gomez.aspx), Professor at Universidad EAFIT.
- [Nicolás Guarín-Zapata](https://github.com/nicoguaro), Researcher at Universidad EAFIT.
- [Juan Carlos Vergara](https://github.com/jvergar2), PhD Student at Universidad EAFIT.

## Instructions

The code is written in Python 2 dialect (we believe that it will work in Python 3 but we have not tested yet) and it depends on numpy, scipy and sympy. TTo use it clone the repo with

    git clone https://github.com/jgomezc1/FEM_PYTHON.git
   
uncompress the zip folder an run the main file in the Python console of your
preference.

## License

This project is licensed under the MIT license. The documents are licensed under Creative Commons Attribution License.

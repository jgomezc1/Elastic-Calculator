# Elastic-Calculator

The Elastic-Calculator allows the visualization of existing elasticity theory solutions using finite element meshes.  In order to visualize a solution the user must execute the script for the problem of interest selected from the provided data-base. Once the problem parameters are defined the script will create a finite element mesh using [Gmsh](http://gmsh.info/) (the free three-dimensional finite element mesh generator) in the background. The closed-form solution, coded in the python module elasticity.py, is then evaluated at the nodes of the finite element assemblage. In order to visualize the solution the mesh is triangulated by the post-processing module plotter.py. The triangulation is directly used by Python to produce an intrpolated image using the nodal field. Solutions different to the ones contained in the repo can also be implemented by adding the specific function to the module elasticity.py.

The repo contains several folders, each one associated to a different solution, and the folder named CALCULATOR containing the modules elasticity.py, plotter.py, generatego.py (with templates for different pre-defined shapes).

The code is written in Python and it depends on numpy and matplotlib. The Gmesh, finite elment meshes are processed with [`meshio`](https://github.com/nschloe/meshio). On the other hand in order to run the problems with the GUI the user needs to install [`easygui`](http://easygui.readthedocs.org/en/master/).  Both modules can be installed with:

    pip install easygui
    pip install meshio

## Authors
- [Juan Carlos Vergara](https://github.com/jvergar2), PhD Student at Universidad EAFIT.
- [Nicolás Guarín-Zapata](https://github.com/nicoguaro), PhD Student at Purdue University.
- [Juan Gomez](http://www.eafit.edu.co/docentes-investigadores/Paginas/juan-gomez.aspx), Professor at Universidad EAFIT.

## Instructions

The code is written in Python 2 dialect (we believe that it will work in Python 3 but we have not tested yet) and it depends on numpy, scipy and sympy. To use it clone the repo with

git clone https://github.com/jgomezc1/Elastic-Calculator
uncompress the zip folder an run the main file in the Python console of your preference.

## License

This project is licensed under the MIT license. The documents are licensed under Creative Commons Attribution License.

# Elastic-Calculator

Template for the elasticity solutions plotter. A user defined solution can be coded in 3 steps:
(i)   Define the model using basic shapes from the geometry generator modulde (generategeo.py) or
      create a new domain (see mygeom). In any case the model is represented by the nodes.txt and
      eles.txt files corresponding to a finite element mesh. These files can be specified directly
      in which case the functions defined in the module generategeo.py are not required.
(ii)  Code your own elasticity solution into the module elasticity.py. See ela.myfunction.
(iii) Plot the solution: use the module plotter.py to plot vector and tensor fields as required.

The repo contains folders defined as follows:

CALCULATOR/ python scripts containing the elasticity solutions, the plotter and model creation subroutines. 

(1). plotter.py    : This is the plotter perse.
(2). elasticity.py : Module that contains the elasticity solution at a given point (x , y).
(3). generatego.py : Module to create nodes.txt and eles.txt files using external meshing tools (GMESH and mesher.for)

# Authors
Juan Carlos Vergara, PhD Student at Universidad EAFIT.
Nicolás Guarín-Zapata, PhD Student at Purdue University.
Juan Gomez, Professor at Universidad EAFIT.

# Instructions

The code is written in Python 2 dialect (we believe that it will work in Python 3 but we have not tested yet) and it depends on numpy, scipy and sympy. To use it clone the repo with

git clone https://github.com/jgomezc1/Elastic-Calculator
uncompress the zip folder an run the main file in the Python console of your preference.

You will also need to install the external code GMESH (http://gmsh.info/)

# License

This project is licensed under the MIT license. The documents are licensed under Creative Commons Attribution License.

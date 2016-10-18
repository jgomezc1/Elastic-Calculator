# Elastic-Calculator
Graphical calculator of fundamental theory of elasticity solutions.
#
Template for the elasticity solutions plotter. A user defined solution can be coded in 3 steps:
(i)   Define the model using basic shapes from the geometry generator modulde (generategeo.py) or
      create a new domain (see mygeom). In any case the model is represented by the nodes.txt and
      eles.txt files corresponding to a finite element mesh. These files can be specified directly
      in which case the functions defined in the module generategeo.py are not required.
(ii)  Code your own elasticity solution into the module elasticity.py. See ela.myfunction.
(iii) Plot the solution: use the module plotter.py to plot vector and tensor fields as required.
---------------------------------------------------------------------------------------------------------
In summary the program requires the following modules:

1. plotter.py    : This is the plotter perse.
2. elasticity.py : Module that contains the elasticity solution at a given point (x , y).
3. generatego.py : Module to create nodes.txt and eles.txt files using external meshing tools (GMESH and mesher.for)

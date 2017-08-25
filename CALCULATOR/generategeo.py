# -*- coding: utf-8 -*-
"""
Mesh generation subroutines
Juan Vergara
Juan Gomez
"""

from os import sys
import numpy as np
import meshio
import os
sys.path.append('../CALCULATOR/')
#

def create_mesh(order , var = '' , seemesh = True):
    orden = str(order)
    os.system ('/Applications/Gmsh.app/Contents/MacOS/gmsh' + ' ' + var + '.geo -2 -order'+ ' ' + orden)
    
    return

#
def writefiles(ietype , var = ''):
    
    points, cells, point_data, cell_data, field_data = \
        meshio.read(var +'.msh')   
    if ietype == 2:
        elements = cells["triangle"]
        els_array = np.zeros([elements.shape[0], 6], dtype=int)
    elif ietype == 9:
        elements = cells["triangle6"]
        els_array = np.zeros([elements.shape[0], 9], dtype=int)
    elif ietype == 3:
        elements = cells["quad"]
        els_array = np.zeros([elements.shape[0], 7], dtype=int)
    els_array[:, 0] = range(elements.shape[0])
    if ietype == 2:
        els_array[:, 1] = 2
    elif ietype == 3:
        els_array[:, 1] = 3
    elif ietype == 9:
        els_array[:, 1] = 9
    els_array[:, 3::] = elements    
    nn = points.shape[0]
    nodes_array = np.zeros([points.shape[0], 3])
    nodes_array[:, 0] = range(points.shape[0])
    nodes_array[:, 1:3] = points[:, :2]
    np.savetxt("eles.txt", els_array, fmt="%d")
    np.savetxt("nodes.txt", nodes_array, fmt=("%d", "%.4f", "%.4f"))
    
    nodes        = np.loadtxt('nodes.txt')
    elements     = np.loadtxt('eles.txt')
    nn =len(nodes[:,0])
    
    return nodes , elements , nn


def ring(r1, r2, c , ietype):
     """
     Creates model.
     geo.ring(a , b , c , ietype)
     c : element size
     ietype = 3 (Bi-linear quad)
     ietype = 9 (Cuadratic triangle)
     ietype = 2 (Linear triangle)
     """
     try:
         import easygui
         var = easygui.enterbox("Enter the job name")

     except:
         var   = raw_input('Enter the job name: ')
     file_name=open(var +'.geo', 'w')
     file_name.write('%22s \n' % ('// Input .geo for Ring'))
     file_name.write('%21s \n' % ('// author: Juan Gomez'))
     file_name.write('%1s \n' % (' '))
     file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))    	
     file_name.write('%0s \n' % (''))    	
     file_name.write('%4s %8.4f %1s \n' % ('r1= ', r1, ';'))    	
     file_name.write('%4s %8.4f %1s \n' % ('r2= ', r2, ';'))   
     file_name.write('%0s \n' % (''))
     file_name.write('%0s \n' % (''))
     file_name.write('%16s \n' % ('// Define points'))
     file_name.write('%0s \n' % (''))
     file_name.write('%42s \n' % ('Point(1) = {0, 0, 0, c};		// {x,y,z, size}'))
     file_name.write('%25s \n' % ('Point(2) = {r1, 0, 0, c};'))
     file_name.write('%25s \n' % ('Point(3) = {r2, 0, 0, c};'))
     file_name.write('%0s \n' % (''))
     file_name.write('%26s \n' % ('// Define boundary circles'))
     file_name.write('%61s \n' % ('Circle(1) = {2, 1, 2};		// {Initial_point, center, end_point}'))
     file_name.write('%22s \n' % ('Circle(2) = {3, 1, 3};'))
     file_name.write('%0s \n' % (''))
     file_name.write('%14s \n' % ('// Joint Lines'))
     file_name.write('%32s \n' % ('Line Loop(1) = {1};	// {Id_line}'))
     file_name.write('%19s \n' % ('Line Loop(2) = {2};'))
     file_name.write('%0s \n' % (''))
     file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
     file_name.write('%26s \n' % ('Plane Surface(1) = {1, 2};'))
    	
     file_name.write('%0s \n' % (''))
     
    	
     file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
     if ietype == 3:
         file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
     else:
         file_name.write('%40s \n' % ('//Recombine Surface {1};			// {Id_Surface}'))
         
    	
     file_name.write('%0s \n' % (''))
    	
     file_name.write('%19s \n' % ('// "Structure" mesh'))
     file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
    	
     file_name.write('%0s \n' % (''))
    
     file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
    	
     file_name.close()
    	
     return var





def mygeom(l, h, c , ietype):
    try:
        import easygui
        var = easygui.enterbox("Enter the job name")

    except:
        var   = raw_input('Enter the job name: ')
    file_name=open(var +'.geo', 'w')
	
    file_name.write('%25s \n' % ('// Input .geo for Boussinesq'))
	
    file_name.write('%21s \n' % ('// author: Juan Gomez'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%3s %6.3f %1s \n' % ('l= ', l, ';'))
	
    file_name.write('%3s %6.3f %1s \n' % ('h= ', h, ';'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%23s \n' % ('// Define vertex points'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%42s \n' % ('Point(1) = {0, 0, 0, c};		// {x,y,z, size}'))
    file_name.write('%26s \n' % ('Point(2) = {l/2, 0, 0, c};'))
    file_name.write('%26s \n' % ('Point(3) = {l/2, h, 0, c};'))
    file_name.write('%27s \n' % ('Point(4) = {-l/2, h, 0, c};'))
    file_name.write('%27s \n' % ('Point(5) = {-l/2, 0, 0, c};'))
	
    file_name.write('%0s \n' % (''))	

    file_name.write('%24s \n' % ('// Define boundary lines'))
    file_name.write('%48s \n' % ('Line(1) = {1, 2};		// {Initial_point, end_point}'))
    file_name.write('%17s \n' % ('Line(2) = {2, 3};'))
    file_name.write('%17s \n' % ('Line(3) = {3, 4};'))
    file_name.write('%17s \n' % ('Line(4) = {4, 5};'))
    file_name.write('%17s \n' % ('Line(5) = {5, 1};'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%14s \n' % ('// Joint Lines'))
    file_name.write('%60s \n' % ('Line Loop(1) = {1, 2, 3, 4, 5};	// {Id_line1,id_line2, ... }'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
    file_name.write('%23s \n' % ('Plane Surface(1) = {1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
    if ietype == 3:
        file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
    else:
        file_name.write('%40s \n' % ('//Recombine Surface {1};			// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// "Structure" mesh'))
    file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
	
    file_name.close()
    
    return var    
#
def wedge(l, fi, c , ietype):
    """
     Creates model.
     geo.ring(a , b , c , ietype)
     c : element size
     ietype = 3 (Bi-linear quad)
     ietype = 9 (Cuadratic triangle)
     ietype = 2 (Linear triangle)
    """
    try:
        import easygui
        var = easygui.enterbox("Enter the job name")

    except:
        var   = raw_input('Enter the job name: ')
    file_name=open(var +'.geo', 'w')
	
    file_name.write('%23s \n' % ('// Input .geo for wedge'))
	
    file_name.write('%21s \n' % ('// author: Juan Gomez'))
	
    file_name.write('%1s \n' % (' '))
	
    file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%3s %40.36f %1s \n' % ('l= ', l, ';'))
	
    file_name.write('%4s %12.8f %1s \n' % ('fi= ', fi, ';'))

    file_name.write('%16s \n' % ('fi= fi*Pi/180.0;'))
	
    file_name.write('%0s \n' % (''))
    file_name.write('%0s \n' % (''))
	
    file_name.write('%23s \n' % ('// Define vertex points'))
    file_name.write('%0s \n' % (''))
	
    file_name.write('%42s \n' % ('Point(1) = {0, 0, 0, c};		// {x,y,z, size}'))
    file_name.write('%59s \n' % ('Point(2) = {-l*Sin(fi), l*Cos(fi), 0, c};		// {x,y,z, size}'))
    file_name.write('%58s \n' % ('Point(3) = {0, 2.0*l*Cos(fi), 0, c};		    // {x,y,z, size}'))
    file_name.write('%58s \n' % ('Point(4) = {l*Sin(fi), l*Cos(fi), 0, c};		// {x,y,z, size}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%24s \n' % ('// Define boundary lines'))
    file_name.write('%48s \n' % ('Line(1) = {1, 2};		// {Initial_point, end_point}'))
    file_name.write('%17s \n' % ('Line(2) = {2, 3};'))
    file_name.write('%17s \n' % ('Line(3) = {3, 4};'))
    file_name.write('%17s \n' % ('Line(4) = {4, 1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%14s \n' % ('// Joint Lines'))
    file_name.write('%57s \n' % ('Line Loop(1) = {1, 2, 3, 4};	// {Id_line1,id_line2, ... }'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
    file_name.write('%23s \n' % ('Plane Surface(1) = {1};'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
    if ietype == 3:
        file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
    else:
        file_name.write('%40s \n' % ('//Recombine Surface {1};			// {Id_Surface}'))


    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// "Structure" mesh'))
    file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
	
    file_name.close()
	
    return var
#

#
def boussinesq(l, h, c , ietype):
    try:
        import easygui
        var = easygui.enterbox("Enter the job name")

    except:
        var   = raw_input('Enter the job name: ')
    file_name=open(var +'.geo', 'w')
	
    file_name.write('%25s \n' % ('// Input .geo for Boussinesq'))
	
    file_name.write('%21s \n' % ('// author: Juan Gomez'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%3s %6.3f %1s \n' % ('l= ', l, ';'))
	
    file_name.write('%3s %6.3f %1s \n' % ('h= ', h, ';'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%23s \n' % ('// Define vertex points'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%42s \n' % ('Point(1) = {0, 0, 0, c};		// {x,y,z, size}'))
    file_name.write('%26s \n' % ('Point(2) = {l/2, 0, 0, c};'))
    file_name.write('%26s \n' % ('Point(3) = {l/2, h, 0, c};'))
    file_name.write('%27s \n' % ('Point(4) = {-l/2, h, 0, c};'))
    file_name.write('%27s \n' % ('Point(5) = {-l/2, 0, 0, c};'))
	
    file_name.write('%0s \n' % (''))	

    file_name.write('%24s \n' % ('// Define boundary lines'))
    file_name.write('%48s \n' % ('Line(1) = {1, 2};		// {Initial_point, end_point}'))
    file_name.write('%17s \n' % ('Line(2) = {2, 3};'))
    file_name.write('%17s \n' % ('Line(3) = {3, 4};'))
    file_name.write('%17s \n' % ('Line(4) = {4, 5};'))
    file_name.write('%17s \n' % ('Line(5) = {5, 1};'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%14s \n' % ('// Joint Lines'))
    file_name.write('%60s \n' % ('Line Loop(1) = {1, 2, 3, 4, 5};	// {Id_line1,id_line2, ... }'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
    file_name.write('%23s \n' % ('Plane Surface(1) = {1};'))
	
    file_name.write('%0s \n' % (''))
	
    if ietype == 3:
        file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
    else:
        file_name.write('%40s \n' % ('//Recombine Surface {1};			// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// "Structure" mesh'))
    file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
	
    file_name.close()
    
    return var
#
def beam(l, h, c , ietype):
    try:
        import easygui
        var = easygui.enterbox("Enter the job name")

    except:
        var   = raw_input('Enter the job name: ')
    file_name=open(var +'.geo', 'w')
	
    file_name.write('%25s \n' % ('// Input .geo for Boussinesq'))
	
    file_name.write('%21s \n' % ('// author: Juan Gomez'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%3s %6.3f %1s \n' % ('l= ', l, ';'))
	
    file_name.write('%3s %6.3f %1s \n' % ('h= ', h, ';'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%23s \n' % ('// Define vertex points'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%42s \n' % ('Point(1) = {0,-h/2, 0, c};		// {x,y,z, size}'))
    file_name.write('%26s \n' % ('Point(2) = {l,-h/2, 0, c};'))
    file_name.write('%26s \n' % ('Point(3) = {l, h/2, 0, c};'))
    file_name.write('%27s \n' % ('Point(4) = {0, h/2, 0, c};'))
	
    file_name.write('%0s \n' % (''))	

    file_name.write('%24s \n' % ('// Define boundary lines'))
    file_name.write('%48s \n' % ('Line(1) = {1, 2};		// {Initial_point, end_point}'))
    file_name.write('%17s \n' % ('Line(2) = {2, 3};'))
    file_name.write('%17s \n' % ('Line(3) = {3, 4};'))
    file_name.write('%17s \n' % ('Line(4) = {4, 1};'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%14s \n' % ('// Joint Lines'))
    file_name.write('%60s \n' % ('Line Loop(1) = {1, 2, 3, 4};	// {Id_line1,id_line2, ... }'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
    file_name.write('%23s \n' % ('Plane Surface(1) = {1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
    if ietype == 3:
        file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
    else:
        file_name.write('%40s \n' % ('//Recombine Surface {1};			// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// "Structure" mesh'))
    file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
	
    file_name.close()
    
    return var
#
def quad(l, h, c , ietype):
    var = raw_input('jobname:--?')
    file_name=open(var +'.geo', 'w')
	
    file_name.write('%25s \n' % ('// Input .geo for quad domain'))
	
    file_name.write('%21s \n' % ('// author: Juan Gomez'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%3s %6.3f %1s \n' % ('l= ', l, ';'))
	
    file_name.write('%3s %6.3f %1s \n' % ('h= ', h, ';'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%23s \n' % ('// Define vertex points'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%42s \n' % ('Point(1) = {-h/2 , 0 , 0, c};		// {x,y,z, size}'))
    file_name.write('%26s \n' % ('Point(2) = {h/2  , 0 , 0, c};'))
    file_name.write('%26s \n' % ('Point(3) = {h/2  , l , 0, c};'))
    file_name.write('%27s \n' % ('Point(4) = {-h/2 , l , 0, c};'))
	
    file_name.write('%0s \n' % (''))	

    file_name.write('%24s \n' % ('// Define boundary lines'))
    file_name.write('%48s \n' % ('Line(1) = {1, 2};		// {Initial_point, end_point}'))
    file_name.write('%17s \n' % ('Line(2) = {2, 3};'))
    file_name.write('%17s \n' % ('Line(3) = {3, 4};'))
    file_name.write('%17s \n' % ('Line(4) = {4, 1};'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%14s \n' % ('// Joint Lines'))
    file_name.write('%60s \n' % ('Line Loop(1) = {1, 2, 3, 4};	// {Id_line1,id_line2, ... }'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
    file_name.write('%23s \n' % ('Plane Surface(1) = {1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
    if ietype == 3:
        file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
    else:
        file_name.write('%40s \n' % ('//Recombine Surface {1};			// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// "Structure" mesh'))
    file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
	
    file_name.close()
    
    return var

#
def canyon(r, l, h, c , ietype):
    try:
        import easygui
        var = easygui.enterbox("Enter the job name")

    except:
        var   = raw_input('Enter the job name: ')
    file_name=open(var +'.geo', 'w')
	
    file_name.write('%40s \n' % ('// Input .geo for circular canyon domain'))
	
    file_name.write('%21s \n' % ('// author: Juan Gomez'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%3s %6.3f %26s \n' % ('r= ', r, '; 		// radio of the canyon'))
	
    file_name.write('%3s %6.3f %22s \n' % ('l= ', l, '; 		 // surface length'))
	
    file_name.write('%3s %6.3f %27s \n' % ('h= ', h, '; 		// height of the domain'))

    file_name.write('%0s \n' % (''))
	
    file_name.write('%23s \n' % ('// Define points'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%46s \n' % ('Point(1) = {-l/2, 0 , 0, c};		// {x,y,z, size}'))
    file_name.write('%26s \n' % ('Point(2) = {-r, 0 , 0, c};'))
    file_name.write('%25s \n' % ('Point(3) = {0, 0 , 0, c};'))
    file_name.write('%25s \n' % ('Point(4) = {r, 0 , 0, c};'))
    file_name.write('%27s \n' % ('Point(5) = {l/2, 0 , 0, c};'))
    file_name.write('%27s \n' % ('Point(6) = {l/2, h , 0, c};'))
    file_name.write('%28s \n' % ('Point(7) = {-l/2, h , 0, c};'))
	
    file_name.write('%0s \n' % (''))	

    file_name.write('%24s \n' % ('// Define boundary lines'))
    file_name.write('%48s \n' % ('Line(1) = {1, 2};		// {Initial_point, end_point}'))
    file_name.write('%17s \n' % ('Line(2) = {4, 5};'))
    file_name.write('%17s \n' % ('Line(3) = {5, 6};'))
    file_name.write('%17s \n' % ('Line(4) = {6, 7};'))
    file_name.write('%17s \n' % ('Line(5) = {7, 1};'))
    file_name.write('%22s \n' % ('Circle(6) = {4, 3, 2};'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%14s \n' % ('// Joint Lines'))
    file_name.write('%66s \n' % ('Line Loop(1) = {1, -6, 2, 3, 4, 5};	// {Id_line1,id_line2, ... }'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
    file_name.write('%23s \n' % ('Plane Surface(1) = {1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
    if ietype == 3:
        file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
    else:
        file_name.write('%40s \n' % ('//Recombine Surface {1};			// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// "Structure" mesh'))
    file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%28s \n' % ('Physical Surface(2000) = {1};'))
	
    file_name.close()
    
    return var


def WedgeDifrac(L1, theta, c):
    
    #L1 is lenght of the wedge, if theta=180° L1 should be minor than 20
    # theta is the inside angle of the wedge 0°<theta<180°
    
    var = raw_input('jobname:--?')
    file_name=open(var +'.geo', 'w')
	
    file_name.write('%23s \n' % ('// Input .geo for wedge'))
	
    file_name.write('%21s \n' % ('// author: Juan Gomez'))
	
    file_name.write('%1s \n' % (' '))
	
    file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%3s %40.36f %1s \n' % ('L1= ', L1, ';'))
	
    file_name.write('%4s %12.8f %1s \n' % ('theta= ', theta, ';'))

    file_name.write('%16s \n' % ('theta= theta*Pi/180.0;'))
	
    file_name.write('%0s \n' % (''))
    file_name.write('%0s \n' % (''))
	
    file_name.write('%23s \n' % ('// Define vertex points'))
    file_name.write('%0s \n' % (''))

	
    file_name.write('%42s \n' % ('Point(1) = {0, L1*Cos(0.5*theta), 0, c};		// {x,y,z, size}'))
    file_name.write('%59s \n' % ('Point(2) = {L1*Sin(0.5*theta), 0, 0, c};		// {x,y,z, size}'))
    file_name.write('%58s \n' % ('Point(3) = {30, 0, 0, c};		// {x,y,z, size}'))
    file_name.write('%58s \n' % ('Point(4) = {30, L1*Cos(0.5*theta)+30, 0, c};		// {x,y,z, size}'))
    file_name.write('%58s \n' % ('Point(5) = {-30, L1*Cos(0.5*theta)+30, 0, c};		// {x,y,z, size}'))
    file_name.write('%58s \n' % ('Point(6) = {-30, 0, 0, c};		// {x,y,z, size}'))
    file_name.write('%58s \n' % ('Point(7) = {-L1*Sin(0.5*theta), 0, 0, c};		// {x,y,z, size}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%24s \n' % ('// Define boundary lines'))
    file_name.write('%48s \n' % ('Line(1) = {1, 2};		// {Initial_point, end_point}'))
    file_name.write('%17s \n' % ('Line(2) = {2, 3};'))
    file_name.write('%17s \n' % ('Line(3) = {3, 4};'))
    file_name.write('%17s \n' % ('Line(4) = {4, 5};'))
    file_name.write('%17s \n' % ('Line(5) = {5, 6};'))
    file_name.write('%17s \n' % ('Line(6) = {6, 7};'))
    file_name.write('%17s \n' % ('Line(7) = {7, 1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%14s \n' % ('// Joint Lines'))
    file_name.write('%57s \n' % ('Line Loop(1) = {1, 2, 3, 4, 5, 6, 7};	// {Id_line1,id_line2, ... }'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
    file_name.write('%23s \n' % ('Plane Surface(1) = {1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
    file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// "Structure" mesh'))
    file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
	
    file_name.close()
	
    return var

def dam(h , c , ietype):
    try:
        import easygui
        var = easygui.enterbox("Enter the job name")

    except:
        var   = raw_input('Enter the job name: ')
    file_name=open(var +'.geo', 'w')
	
    file_name.write('%23s \n' % ('// Input .geo for DAM'))
	
    file_name.write('%21s \n' % ('// author: Flaco Sierra'))
	
    file_name.write('%1s \n' % (' '))
	
    file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%4s %12.8f %1s \n' % ('h= ', h, ';'))
	
    file_name.write('%0s \n' % (''))
    file_name.write('%0s \n' % (''))
	
    file_name.write('%23s \n' % ('// Define vertex points'))
    file_name.write('%0s \n' % (''))
	
    file_name.write('%42s \n' % ('Point(1) = {0, 0, 0, c};		// {x,y,z, size}'))
    file_name.write('%59s \n' % ('Point(2) = {h, 0, 0, c};		// {x,y,z, size}'))
    file_name.write('%58s \n' % ('Point(3) = {h, h, 0, c};		    // {x,y,z, size}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%24s \n' % ('// Define boundary lines'))
    file_name.write('%48s \n' % ('Line(1) = {1, 2};		// {Initial_point, end_point}'))
    file_name.write('%17s \n' % ('Line(2) = {2, 3};'))
    file_name.write('%17s \n' % ('Line(3) = {3, 1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%14s \n' % ('// Joint Lines'))
    file_name.write('%57s \n' % ('Line Loop(1) = {1, 2, 3};	// {Id_line1,id_line2, ... }'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
    file_name.write('%23s \n' % ('Plane Surface(1) = {1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
    if ietype == 3:
        file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
    else:
        file_name.write('%40s \n' % ('//Recombine Surface {1};			// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// "Structure" mesh'))
    file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
	
    file_name.close()
	
    return var


def memb(l, h, c , ietype):
    var = raw_input('jobname:--?')
    file_name=open(var +'.geo', 'w')
	
    file_name.write('%25s \n' % ('// Input .geo for quad domain'))
	
    file_name.write('%21s \n' % ('// author: Juan Gomez'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%4s %6.3f %25s \n' % ('c = ', c, '; 		// for size elements'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%3s %6.3f %1s \n' % ('l= ', l, ';'))
	
    file_name.write('%3s %6.3f %1s \n' % ('h= ', h, ';'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%23s \n' % ('// Define vertex points'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%42s \n' % ('Point(1) = {0 , 0 , 0, c};		// {x,y,z, size}'))
    file_name.write('%26s \n' % ('Point(2) = {h  , 0 , 0, c};'))
    file_name.write('%26s \n' % ('Point(3) = {h  , l , 0, c};'))
    file_name.write('%27s \n' % ('Point(4) = {0 , l , 0, c};'))
	
    file_name.write('%0s \n' % (''))	

    file_name.write('%24s \n' % ('// Define boundary lines'))
    file_name.write('%48s \n' % ('Line(1) = {1, 2};		// {Initial_point, end_point}'))
    file_name.write('%17s \n' % ('Line(2) = {2, 3};'))
    file_name.write('%17s \n' % ('Line(3) = {3, 4};'))
    file_name.write('%17s \n' % ('Line(4) = {4, 1};'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%14s \n' % ('// Joint Lines'))
    file_name.write('%60s \n' % ('Line Loop(1) = {1, 2, 3, 4};	// {Id_line1,id_line2, ... }'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%35s \n' % ('// surface for mesh 			// {Id_Loop}'))
    file_name.write('%23s \n' % ('Plane Surface(1) = {1};'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// For Mesh 4 nodes'))
    if ietype == 3:
        file_name.write('%40s \n' % ('Recombine Surface {1};			// {Id_Surface}'))
    else:
        file_name.write('%40s \n' % ('//Recombine Surface {1};			// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))
	
    file_name.write('%19s \n' % ('// "Structure" mesh'))
    file_name.write('%41s \n' % ('Transfinite Surface {1};		// {Id_Surface}'))
	
    file_name.write('%0s \n' % (''))

    file_name.write('%28s \n' % ('Physical Surface(100) = {1};'))
	
    file_name.close()
    
    return var














































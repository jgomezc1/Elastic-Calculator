  // Input .geo for DAM 
// author: Flaco Sierra 
  
c =   0.150  ; 		// for size elements 
 
 h=   10.00000000 ; 
 
 
// Define vertex points 
 
Point(1) = {0, 0, 0, c};		// {x,y,z, size} 
                 Point(2) = {h, 0, 0, c};		// {x,y,z, size} 
            Point(3) = {h, h, 0, c};		    // {x,y,z, size} 
 
// Define boundary lines 
Line(1) = {1, 2};		// {Initial_point, end_point} 
Line(2) = {2, 3}; 
Line(3) = {3, 1}; 
 
// Joint Lines 
   Line Loop(1) = {1, 2, 3};	// {Id_line1,id_line2, ... } 
 
// surface for mesh 			// {Id_Loop} 
Plane Surface(1) = {1}; 
 
// For Mesh 4 nodes 
Recombine Surface {1};			// {Id_Surface} 
 
// "Structure" mesh 
Transfinite Surface {1};		// {Id_Surface} 
 
Physical Surface(100) = {1}; 

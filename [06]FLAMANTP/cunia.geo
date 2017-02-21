// Input .geo for wedge 
// author: Juan Gomez 
  
c =   0.100  ; 		// for size elements 
 
l=    1.000000000000000000000000000000000000 ; 
fi=   45.00000000 ; 
fi= fi*Pi/180.0; 
 
 
// Define vertex points 
 
Point(1) = {0, 0, 0, c};		// {x,y,z, size} 
Point(2) = {-l*Sin(fi), l*Cos(fi), 0, c};		// {x,y,z, size} 
Point(3) = {0, 2.0*l*Cos(fi), 0, c};		    // {x,y,z, size} 
Point(4) = {l*Sin(fi), l*Cos(fi), 0, c};		// {x,y,z, size} 
 
// Define boundary lines 
Line(1) = {1, 2};		// {Initial_point, end_point} 
Line(2) = {2, 3}; 
Line(3) = {3, 4}; 
Line(4) = {4, 1}; 
 
// Joint Lines 
Line Loop(1) = {1, 2, 3, 4};	// {Id_line1,id_line2, ... } 
 
// surface for mesh 			// {Id_Loop} 
Plane Surface(1) = {1}; 
 
// For Mesh 4 nodes 
Recombine Surface {1};			// {Id_Surface} 
 
// "Structure" mesh 
Transfinite Surface {1};		// {Id_Surface} 
 
Physical Surface(100) = {1}; 

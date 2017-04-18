// Input .geo for Ring 
// author: Juan Gomez 
  
c =   0.150  ; 		// for size elements 
 
r1=    2.0000 ; 
r2=    3.0000 ; 
 
 
// Define points 
 
Point(1) = {0, 0, 0, c};		// {x,y,z, size} 
Point(2) = {r1, 0, 0, c}; 
Point(3) = {r2, 0, 0, c}; 
 
// Define boundary circles 
Circle(1) = {2, 1, 2};		// {Initial_point, center, end_point} 
Circle(2) = {3, 1, 3}; 
 
// Joint Lines 
Line Loop(1) = {1};	// {Id_line} 
Line Loop(2) = {2}; 
 
// surface for mesh 			// {Id_Loop} 
Plane Surface(1) = {1, 2}; 
 
// For Mesh 4 nodes 
//Recombine Surface {1};			// {Id_Surface} 
 
// "Structure" mesh 
Transfinite Surface {1};		// {Id_Surface} 
 
Physical Surface(100) = {1}; 

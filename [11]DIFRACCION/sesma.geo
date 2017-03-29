// Input .geo for wedge 
// author: Juan Gomez 
  
c =   1.200  ; 		// for size elements 
 
L1=   20.000000000000000000000000000000000000 ; 
theta=   90.00000000 ; 
theta= theta*Pi/180.0; 
 
 
// Define vertex points 
 
Point(1) = {0, L1*Cos(0.5*theta), 0, c};		// {x,y,z, size} 
 Point(2) = {L1*Sin(0.5*theta), 0, 0, c};		// {x,y,z, size} 
               Point(3) = {30, 0, 0, c};		// {x,y,z, size} 
Point(4) = {30, L1*Cos(0.5*theta)+30, 0, c};		// {x,y,z, size} 
Point(5) = {-30, L1*Cos(0.5*theta)+30, 0, c};		// {x,y,z, size} 
              Point(6) = {-30, 0, 0, c};		// {x,y,z, size} 
Point(7) = {-L1*Sin(0.5*theta), 0, 0, c};		// {x,y,z, size} 
 
// Define boundary lines 
Line(1) = {1, 2};		// {Initial_point, end_point} 
Line(2) = {2, 3}; 
Line(3) = {3, 4}; 
Line(4) = {4, 5}; 
Line(5) = {5, 6}; 
Line(6) = {6, 7}; 
Line(7) = {7, 1}; 
 
// Joint Lines 
Line Loop(1) = {1, 2, 3, 4, 5, 6, 7};	// {Id_line1,id_line2, ... } 
 
// surface for mesh 			// {Id_Loop} 
Plane Surface(1) = {1}; 
 
// For Mesh 4 nodes 
Recombine Surface {1};			// {Id_Surface} 
 
// "Structure" mesh 
Transfinite Surface {1};		// {Id_Surface} 
 
Physical Surface(100) = {1}; 

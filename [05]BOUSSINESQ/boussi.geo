// Input .geo for Boussinesq 
// author: Juan Gomez 
 
c =   0.200  ; 		// for size elements 
 
l=  10.000 ; 
h=  10.000 ; 
 
// Define vertex points 
 
Point(1) = {0, 0, 0, c};		// {x,y,z, size} 
Point(2) = {l/2, 0, 0, c}; 
Point(3) = {l/2, h, 0, c}; 
Point(4) = {-l/2, h, 0, c}; 
Point(5) = {-l/2, 0, 0, c}; 
 
// Define boundary lines 
Line(1) = {1, 2};		// {Initial_point, end_point} 
Line(2) = {2, 3}; 
Line(3) = {3, 4}; 
Line(4) = {4, 5}; 
Line(5) = {5, 1}; 
 
// Joint Lines 
Line Loop(1) = {1, 2, 3, 4, 5};	// {Id_line1,id_line2, ... } 
 
// surface for mesh 			// {Id_Loop} 
Plane Surface(1) = {1}; 
 
Recombine Surface {1};			// {Id_Surface} 
 
// "Structure" mesh 
Transfinite Surface {1};		// {Id_Surface} 
 
Physical Surface(100) = {1}; 

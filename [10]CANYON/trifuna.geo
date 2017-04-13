// Input .geo for circular canyon domain 
// author: Juan Gomez 
 
c =   0.150  ; 		// for size elements 
 
r=   1.000 ; 		// radio of the canyon 
l=   5.000 ; 		 // surface length 
h=  10.000 ; 		// height of the domain 
 
       // Define points 
 
Point(1) = {-l/2, 0 , 0, c};		// {x,y,z, size} 
Point(2) = {-r, 0 , 0, c}; 
Point(3) = {0, 0 , 0, c}; 
Point(4) = {r, 0 , 0, c}; 
Point(5) = {l/2, 0 , 0, c}; 
Point(6) = {l/2, h , 0, c}; 
Point(7) = {-l/2, h , 0, c}; 
 
// Define boundary lines 
Line(1) = {1, 2};		// {Initial_point, end_point} 
Line(2) = {4, 5}; 
Line(3) = {5, 6}; 
Line(4) = {6, 7}; 
Line(5) = {7, 1}; 
Circle(6) = {4, 3, 2}; 
 
// Joint Lines 
  Line Loop(1) = {1, -6, 2, 3, 4, 5};	// {Id_line1,id_line2, ... } 
 
// surface for mesh 			// {Id_Loop} 
Plane Surface(1) = {1}; 
 
// For Mesh 4 nodes 
//Recombine Surface {1};			// {Id_Surface} 
 
// "Structure" mesh 
Transfinite Surface {1};		// {Id_Surface} 
 
Physical Surface(2000) = {1}; 

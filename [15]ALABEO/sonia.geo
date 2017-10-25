// .geo para eje de perfil eliptico 
// autor: Sonia C. Garcia 
 
c =   0.100 ; 		// Tamaño de los elementos 
 
a=   1.000 ; 		// Eje mayor 
b=   1.000 ; 		// Eje menor 
 
// Definiendo los puntos 
 
Point(1) = {0 , 0 , 0, c};		// {x,y,z, size} 
Point(2) = {a  , 0 , 0, c}; 
Point(3) = {-a  , 0 , 0, c}; 
 Point(4) = {0 , b , 0, c}; 
Point(5) = {0 , -b , 0, c}; 
 
// Definiendo las líneas de frontera 
                      Ellipse(1) = {2, 1, 3, 4}; 
Ellipse(2) = {4, 1, 3, 3}; 
Ellipse(3) = {3, 1, 2, 5}; 
Ellipse(4) = {5, 1, 2, 2}; 
 
// Juntando las líneas 
   Line Loop(1) = {1, 2, 3, 4};	// {Id_line1,id_line2, ... } 
 
// surface for mesh 			// {Id_Loop} 
Plane Surface(1) = {1}; 
 
// For Mesh 4 nodes 
Recombine Surface {1};			// {Id_Surface} 
 
// "Structure" mesh 
Transfinite Surface {1};		// {Id_Surface} 
 
Physical Surface(100) = {1}; 

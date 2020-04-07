# Path Planning for a Rover in 3D Space

The goal of the project was to find the most optimal path that a rover should take from a landing site to multiple target sites given a 3D space terrain map with obstacles by using search algorithms. The complete program was developed in Python.

This code was among the top 5% in terms of speed and efficiency in CSCI 561 - Foundations of Artificial Intelligence, USC Fall 2019 class.

Input:The file input.txt in the current directory of your program will be formatted as follows:

First line: Instruction of which algorithm to use, asa string: BFS, UCSor A*
Second line: Two strictly positive 32-bit integers separated by one space character, for“W H” the number of columns (width)and rows (height), in cells,of the map.
Thirdline: Two positive 32-bit integers separated by one space character, for“XY” the coordinates(in cells)of the landing site. 0 £X £W-1 and 0 £Y £H-1(that is, we use 0-based indexing into the map; X increases when moving East and Y increases when moving South; (0,0) is the North West corner of the map).
Fourthline: Positive 32-bit integernumber for the maximum difference in elevation betweentwo adjacent cells which the rover can drive over.The difference in Z between two adjacent cells must be smallerthan or equal(£)to this value for the rover to be ableto travelfrom one cell to the other.
Fifthline: Strictly positive 32-bit integer N, the number of target sites.
Next Nlines: Two positive 32-bit integers separated by one space character, for“X Y” the coordinates (in cells)of each target site. 0<=X <=W-1 and 0<=Y<=H-1(that is, we again use 0-based indexing into the map).
Next Hlines: W 32-bit integernumbers separated by any numbers of spaces for the elevation (Z) values ofeach of the W cells in each row of the map.

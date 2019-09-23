# MATH482-InstantInsanity
This is a project I did with my team for Math 482 at CSUN to solve Instant Insanity puzzles. 
It is a brute-force approach to look for the minimal obstacle if a solution is not found.


Designing a computer program to search for “obstacles,” if they exist, for Instant Insanity puzzles of size 30 cubes. 
If an obstacle exists find the smallest one. Obstacle refer to a subset of the cubes, which cannot be part of any solution. 
I.e., any stacking of these cubes entails at least one side having some color showing up two or more times. 
For instance if a given puzzle has two monochromatic cubes of the same color then that puzzle has an obstacle of size two. 
You have free reign over what type of algorithm to use, but I would prefer for you to write the program in Python as it will be easier for me to understand. 
A brute-force algorithm (depth or breadth first search through the tree of possible selections) may work fine for puzzles without solutions of size less than 10 cubes. But in getting to size 30 the combinatorial explosion of possibilities may require some special considerations. 
Observing that a particular color only shows up three times is not the same as identifying the smallest obstacle. 
For this project we are looking for obstacles, not solving puzzles that have solutions. 
In case a solution was there then we simply provide the solution.

This routine will fill in the colors in sequence: (cube1 opposite pair 1 left, cube1 opposite pair 1 right, cube1 opposite pair 2 left, cube1 opposite pair 2 right, cube1 opposite pair 3 left, cube1 opposite pair 3 right, cube2 opposite pair 1 left, cube2 opposite pair 1 right, cube2 opposite pair 2 left, … , cube30 opposite pair 3 left, cube30 opposite pair 3 right).

The color-generating assignment formulae are:
1 + ((floor n𝜋) mod 30),	1 ≤ n ≤ 180, for puzzle one, 1 + ((floor n𝑒) mod 30),	1 ≤ n ≤ 180, for puzzle two,
1 +	floor 𝑛	mod 30 , 1 ≤ n ≤ 180, for puzzle three,

1 +	floor 𝑛	mod 30 , 1 ≤ n ≤ 180, for puzzle four.

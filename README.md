# 8-Puzzel solver using search algorithm

#Introduction#
Welcome to the 8 Puzzle Solver project, a Python implementation of a classic problem-solving algorithm. This project aims to provide a simple and efficient solution to the 8 puzzle problem using various search algorithms.

#Project Overview
The 8 puzzle problem is a classic problem in the field of artificial intelligence and computer science. The problem consists of a 3x3 grid with 8 numbered tiles and one blank space. The goal is to rearrange the tiles to form a specific configuration, usually the goal state, using a set of allowed moves.

This project implements the following search algorithms to solve the 8 puzzle problem:

Breadth-First Search (BFS)
Depth-First Search (DFS)
A* Search
Greedy Search
#Usage Instructions
To use the 8 Puzzle Solver, follow these steps:

1)Clone the repository to your local machine.
2)Install the required dependencies by running pip install -r requirements.txt in your terminal.
3)Run the program by executing python main.py in your terminal.
4)Select the search algorithm you want to use by entering the corresponding number:
  1: Breadth-First Search (BFS)
  2: Depth-First Search (DFS)
  3: A* Search
5)The program will display the nodes visited,time taken, memory used and the number of steps required to reach the goal state.

#Search Algorithms
The following search algorithms are implemented in this project:

Breadth-First Search (BFS): Explores all the nodes at the current depth level before moving on to the next depth level.
Depth-First Search (DFS): Explores as far as possible along each branch before backtracking.
A* Search: Uses an admissible heuristic function to guide the search towards the goal state.

#Running the Program
To run the program, execute the following command in your terminal:

bash
python 8puzzle1.py
Verify

Open In Editor
Run
Copy code
8puzzle1.py
Troubleshooting
If you encounter any issues while running the program, check the following:

Make sure you have installed the required dependencies.
Check that you have entered the initial and goal states correctly.
If the program is taking too long to run, try reducing the size of the puzzle or using a more efficient search algorithm.

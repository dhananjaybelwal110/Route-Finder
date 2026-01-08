#🗺️ Route Finder Project using Python

## 📌 Project Overview
The Route Finder Project is a Python-based application that finds all possible routes and the shortest route between two cities using graph algorithms.
It demonstrates the practical application of Data Structures and Algorithms (DSA) such as Depth First Search (DFS) and Dijkstra’s Algorithm on a weighted graph.

This project is suitable for college submission, viva examinations, and GitHub portfolios.


##🎯 Objectives
- To represent cities and routes using a graph data structure
- To find all possible paths between two cities
- To determine the shortest path based on distance
- To apply core DSA concepts in a real-world problem
- To design a modular and maintainable Python project


##🧠 Algorithms & Concepts Used
- Graph (Adjacency List)
- Depth First Search (DFS)
- Backtracking
- Dijkstra’s Algorithm
- Priority Queue (Heap)
- Dictionaries and Sets


##⚙️ Features
- User-defined cities and routes
- Displays all possible paths between source and destination
- Calculates distance for each path
- Finds the shortest path with minimum total distance
- Clean console output
- Modular file structure (easy to understand and extend)


##📁 Project Structure

Route-Finder-Project/
│
├── main.py
├── graph_input.py
├── dfs_paths.py
├── dijkstra.py
├── utils.py
├── sample_input.txt
└── README.txt


##▶️ How to Run the Project

Keep sample_input.txt in the same folder as main.py.

Add the following lines at the top of main.py:

import sys
sys.stdin = open("sample_input.txt")

Run the program:
python main.py


##🧪 Sample Input

5
A
B
C
D
E
6
A B 4
A C 2
B C 5
B D 10
C E 3
E D 4
A
D


##📤 Sample Output

ALL POSSIBLE PATHS:
1. A → B → D | Distance: 14
2. A → B → C → E → D | Distance: 16
3. A → C → E → D | Distance: 9

SHORTEST PATH (DIJKSTRA):
A → C → E → D
Total Distance: 9

---

## Author
Dhananjay Belwal



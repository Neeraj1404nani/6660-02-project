import tkinter as tk
from tkinter import messagebox
from collections import deque
import heapq
import time
import tracemalloc


class PuzzleSolver:
    def __init__(self, root, start, goal):
        self.root = root
        self.root.title("Eight Puzzle Solver")
        self.start = start
        self.goal = goal
        self.goal_tuple = tuple(tuple(row) for row in goal)
        self.tiles = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()
        self.update_grid(self.start)
    def create_widgets(self):
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(pady=20)
        for i in range(3):
            for j in range(3):
                tile = tk.Label(self.grid_frame, text="", font=("Arial", 24), width=4, height=2, borderwidth=2,
                                relief="solid")
                tile.grid(row=i, column=j)
                self.tiles[i][j] = tile
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=20)

        self.bfs_button = tk.Button(self.control_frame, text="Solve with BFS", command=self.bfs)
        self.bfs_button.grid(row=0, column=0, padx=5)

        self.dfs_button = tk.Button(self.control_frame, text="Solve with DFS", command=self.dfs)
        self.dfs_button.grid(row=0, column=1, padx=5)

        self.a_star_button = tk.Button(self.control_frame, text="Solve with A*", command=self.a_star)
        self.a_star_button.grid(row=0, column=2, padx=5)

        self.reset_button = tk.Button(self.control_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=0, column=3, padx=5)

    def update_grid(self, state):
        for i in range(3):
            for j in range(3):
                val = state[i][j]
                self.tiles[i][j].config(text=str(val) if val != 0 else "", bg="white" if val != 0 else "tan")

    def reset(self):
        self.update_grid(self.start)

    def get_neighbors(self, state):
        neighbors = []
        row, col = next((r, c) for r, row in enumerate(state) for c, val in enumerate(row) if val == 0)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [list(row) for row in state]
                new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                neighbors.append(new_state)
        return neighbors

    def animate_solution(self, path):
        for step in path:
            self.update_grid(step)
            self.root.update()
            time.sleep(0.5)

    def print_results(self, came_from, current, nodes_visited, duration, memory_used):
        path = []
        while current:
            path.append(current)
            current = came_from[current]
        path.reverse()
        steps = len(path) - 1
        messagebox.showinfo("Solution", f"Solution found in {steps} steps!\n"
                                        f"Nodes Visited: {nodes_visited}\n"
                                        f"Time Taken: {duration:.4f} seconds\n"
                                        f"Memory Used: {memory_used / 1024:.2f} KB")
        self.animate_solution(path)

    def bfs(self):
        tracemalloc.start()
        start_time = time.time()
        first = tuple(tuple(row) for row in self.start)
        queue = deque([first])
        path = {first: None}
        visited = set()
        nodes_visited = 0

        while queue:
            current = queue.popleft()
            nodes_visited += 1
            if current == self.goal_tuple:
                duration = time.time() - start_time
                memory_used = tracemalloc.get_traced_memory()[1]
                tracemalloc.stop()
                self.print_results(path, current, nodes_visited, duration, memory_used)
                return
            visited.add(current)
            for neighbor in self.get_neighbors(current):
                neighbor_tuple = tuple(tuple(row) for row in neighbor)
                if neighbor_tuple not in visited and neighbor_tuple not in path:
                    queue.append(neighbor_tuple)
                    path[neighbor_tuple] = current
        messagebox.showinfo("Result", "No Solution Found with BFS")

    def dfs(self):
        tracemalloc.start()
        start_time = time.time()
        first = tuple(tuple(row) for row in self.start)
        stack = [first]
        path = {first: None}
        visited = set()
        nodes_visited = 0

        while stack:
            current = stack.pop()
            nodes_visited += 1
            if current == self.goal_tuple:
                duration = time.time() - start_time
                memory_used = tracemalloc.get_traced_memory()[1]
                tracemalloc.stop()
                self.print_results(path, current, nodes_visited, duration, memory_used)
                return
            visited.add(current)
            for neighbor in self.get_neighbors(current):
                neighbor_tuple = tuple(tuple(row) for row in neighbor)
                if neighbor_tuple not in visited and neighbor_tuple not in path:
                    stack.append(neighbor_tuple)
                    path[neighbor_tuple] = current
        messagebox.showinfo("Result", "No Solution Found with DFS")

    def heuristic(self, state):
        return sum(abs(r1 - r2) + abs(c1 - c2)
                   for r1, row in enumerate(state) for c1, val in enumerate(row) if val != 0
                   for r2, row_goal in enumerate(self.goal) for c2, goal_val in enumerate(row_goal) if goal_val == val)

    def a_star(self):
        tracemalloc.start()
        start_time = time.time()
        first = tuple(tuple(row) for row in self.start)
        open_set = [(self.heuristic(self.start), first)]
        path = {first: None}
        g_score = {first: 0}
        nodes_visited = 0

        while open_set:
            _, current = heapq.heappop(open_set)
            nodes_visited += 1
            if current == self.goal_tuple:
                duration = time.time() - start_time
                memory_used = tracemalloc.get_traced_memory()[1]
                tracemalloc.stop()
                self.print_results(path, current, nodes_visited, duration, memory_used)
                return
            for neighbor in self.get_neighbors(current):
                neighbor_tuple = tuple(tuple(row) for row in neighbor)
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score.get(neighbor_tuple, float('inf')):
                    path[neighbor_tuple] = current
                    g_score[neighbor_tuple] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor)
                    heapq.heappush(open_set, (f_score, neighbor_tuple))
        messagebox.showinfo("Result", "No Solution Found with A*")


# Initialize puzzle state and run GUI
start = [
    [5, 4, 2],
    [7, 1, 3],
    [0, 8, 6]
]
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

root = tk.Tk()
app = PuzzleSolver(root, start, goal)
root.mainloop()

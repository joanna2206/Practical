#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt

class GraphColoring:
    def __init__(self, graph, num_colors):
        self.graph = graph
        self.num_vertices = len(graph)
        self.num_colors = num_colors
        self.colors = [-1] * self.num_vertices

    def is_safe(self, vertex, color):
        """Check if it's safe to assign the color to the vertex."""
        for neighbor in self.graph[vertex]:
            if self.colors[neighbor] == color:
                return False
        return True

    def backtrack(self, vertex):
        """Try to assign a color to the vertex and backtrack if needed."""
        if vertex == self.num_vertices:
            return True
        for color in range(self.num_colors):
            if self.is_safe(vertex, color):
                self.colors[vertex] = color
                if self.backtrack(vertex + 1):
                    return True
                self.colors[vertex] = -1
        return False

    def branch_and_bound(self, vertex, color_bound):
        """Branch and Bound approach with backtracking."""
        if vertex == self.num_vertices:
            return True
        if color_bound >= self.num_colors:
            return False
        for color in range(self.num_colors):
            if self.is_safe(vertex, color):
                self.colors[vertex] = color
                if self.branch_and_bound(vertex + 1, color_bound):
                    return True
                self.colors[vertex] = -1
        return False

    def solve(self, use_branch_and_bound=False):
        """Solve the graph coloring problem."""
        print(f"Solving with {'Branch and Bound' if use_branch_and_bound else 'Backtracking'}...")
        if use_branch_and_bound:
            if not self.branch_and_bound(0, 0):
                return None
        else:
            if not self.backtrack(0):
                return None
        return self.colors

    def visualize(self):
        """Visualize the graph with the assigned colors."""
        if not self.colors or all(c == -1 for c in self.colors):
            print("Cannot visualize: No valid coloring found.")
            return
        G = nx.Graph()
        for i in range(self.num_vertices):
            G.add_node(i)
        for i in range(self.num_vertices):
            for neighbor in self.graph[i]:
                G.add_edge(i, neighbor)
        color_names = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'cyan', 'brown', 'gray']
        node_colors = [color_names[self.colors[i] % len(color_names)] for i in range(self.num_vertices)]
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=600, font_weight='bold')
        plt.title("Graph Coloring Visualization")
        plt.show()

def get_graph_from_user():
    """Function to get the graph from the user with input validation."""
    try:
        num_vertices = int(input("Enter the number of vertices: "))
        if num_vertices <= 0:
            raise ValueError("Number of vertices must be positive.")
        edges = int(input("Enter the number of edges: "))
        if edges < 0:
            raise ValueError("Number of edges cannot be negative.")
        graph = [[] for _ in range(num_vertices)]
        print("Enter the edges (format: vertex1 vertex2):")
        for _ in range(edges):
            u, v = map(int, input().split())
            if u < 0 or u >= num_vertices or v < 0 or v >= num_vertices:
                raise ValueError(f"Vertex indices must be between 0 and {num_vertices - 1}.")
            graph[u].append(v)
            graph[v].append(u)
        return graph, num_vertices
    except ValueError as e:
        print(f"Error: {e}")
        return None, None

def main():
    try:
        graph, num_vertices = get_graph_from_user()
        if graph is None:
            print("Invalid graph input. Try again.")
            return
        try:
            num_colors = int(input("Enter the number of colors: "))
            if num_colors <= 0:
                raise ValueError("Number of colors must be positive.")
        except ValueError:
            print("Error: Number of colors must be a positive integer.")
            return
        graph_coloring = GraphColoring(graph, num_colors)
        method = input("Would you like to use Backtracking or Branch and Bound? (Enter 'backtracking' or 'branch_and_bound'): ").strip().lower()
        if method == "backtracking":
            solution = graph_coloring.solve(use_branch_and_bound=False)
            method_used = "Backtracking"
        elif method == "branch_and_bound":
            solution = graph_coloring.solve(use_branch_and_bound=True)
            method_used = "Branch and Bound"
        else:
            print("Invalid method. Please choose either 'backtracking' or 'branch_and_bound'.")
            return
        if solution:
            print(f"\nGraph coloring solution ({method_used}): {solution}")
            graph_coloring.visualize()
        else:
            print(f"No solution found using {method_used}. Try increasing the number of colors.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    while True:
        try:
            main()
            if input("Run again? (yes/no): ").strip().lower() != 'yes':
                break
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break


# In[ ]:





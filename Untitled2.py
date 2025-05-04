#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_result = []  # To store the BFS result
    print("\nStarting BFS traversal:")
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_result.append(node)
            print(f"Visited: {node}")
        # Queue the neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
        print(f"Queue after visiting {node}: {list(queue)}")
    return bfs_result

# DFS function
def dfs(graph, start):
    visited = set()
    stack = [start]
    dfs_result = []  # To store the DFS result
    print("\nStarting DFS traversal:")
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            dfs_result.append(node)
            print(f"Visited: {node}")
        # Push the neighbors to the stack (in reverse order for correct traversal)
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)
        print(f"Stack after visiting {node}: {list(stack)}")
    return dfs_result

# Input function to create a graph
def input_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges in the graph: "))
    print("Enter edges in the format: U V: ")
    for _ in range(num_edges):
        node1, node2 = input().split()
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph

# Function to display the graph
def display_graph(graph):
    print("\nGraph representation: ")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

# Function to visualize the graph
def visualize_graph(graph):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    # Draw the graph using matplotlib
    plt.figure(figsize=(8,6))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=3000, font_size=15)
    plt.title("Graph Visualization")
    plt.show()

# Main function
if __name__ == "__main__":
    print("Graph Traversal Program (BFS and DFS)")
    # Input graph from the user
    graph = input_graph()
    # Display graph structure
    display_graph(graph)
    # Visualize the graph
    visualize_graph(graph)
    # Starting node input
    start_node = input("Enter the starting node for BFS and DFS: ")
    # BFS and result
    bfs_result = bfs(graph, start_node)
    print(f"\nFinal BFS Traversal Order: {bfs_result}")
    # DFS and result
    dfs_result = dfs(graph, start_node)
    print(f"\nFinal DFS Traversal Order: {dfs_result}")


# In[ ]:





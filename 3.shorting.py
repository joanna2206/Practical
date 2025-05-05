#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import defaultdict

def get_graph_from_user():
    """Get graph details from the user with input validation."""
    try:
        num_vertices = int(input("Enter the number of vertices: "))
        if num_vertices <= 0:
            raise ValueError("Number of vertices must be positive.")
        num_edges = int(input("Enter the number of edges: "))
        if num_edges < 0:
            raise ValueError("Number of edges cannot be negative.")
        graph = [[] for _ in range(num_vertices)]
        edges = []
        print("Enter the edges (format: source destination weight):")
        for _ in range(num_edges):
            u, v, w = map(int, input().split())
            if u < 0 or u >= num_vertices or v < 0 or v >= num_vertices:
                raise ValueError(f"Vertex indices must be between 0 and {num_vertices - 1}.")
            if w < 0:
                raise ValueError("Edge weight cannot be negative.")
            graph[u].append((v, w))
            graph[v].append((u, w))  # Undirected graph
            edges.append((u, v, w))
        return graph, num_vertices, edges
    except ValueError as e:
        print(f"Error: {e}")
        return None, None, None

def selection_sort():
    """Implement Selection Sort with user input."""
    try:
        arr = list(map(int, input("Enter numbers to sort (space-separated): ").split()))
        if not arr:
            print("Empty array provided.")
            return
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print("Sorted array:", arr)
    except ValueError:
        print("Error: Please enter valid integers.")

def prim_mst():
    """Implement Prim's MST algorithm with visualization."""
    graph, num_vertices, _ = get_graph_from_user()
    if graph is None:
        return
    parent = [None] * num_vertices
    key = [float('inf')] * num_vertices
    mst_set = [False] * num_vertices
    key[0] = 0
    parent[0] = -1
    pq = [(0, 0)]  # (weight, vertex)

    while pq:
        w, u = heapq.heappop(pq)
        if mst_set[u]:
            continue
        mst_set[u] = True
        for v, weight in graph[u]:
            if not mst_set[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(pq, (weight, v))

    mst_edges = [(parent[i], i, key[i]) for i in range(1, num_vertices) if parent[i] is not None]
    print("Minimum Spanning Tree (Prim's):")
    total_weight = sum(w for _, _, w in mst_edges)
    for u, v, w in mst_edges:
        print(f"Edge: {u} - {v}, Weight: {w}")
    print(f"Total MST weight: {total_weight}")

    # Visualization
    G = nx.Graph()
    for u in range(num_vertices):
        G.add_node(u)
    edge_labels = {}
    for u in range(num_vertices):
        for v, w in graph[u]:
            if v > u:
                G.add_edge(u, v, weight=w)
                edge_labels[(u, v)] = w
    mst_edge_list = [(u, v) for u, v, _ in mst_edges]
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_edges(G, pos, edgelist=mst_edge_list, edge_color='red', width=2)
    plt.title("Prim's Minimum Spanning Tree (Red Edges)")
    plt.show()

def kruskal_mst():
    """Implement Kruskal's MST algorithm with visualization."""
    graph, num_vertices, edges = get_graph_from_user()
    if graph is None:
        return
    parent = list(range(num_vertices))
    rank = [0] * num_vertices

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        pu, pv = find(u), find(v)
        if pu == pv:
            return
        if rank[pu] < rank[pv]:
            parent[pu] = pv
        elif rank[pu] > rank[pv]:
            parent[pv] = pu
        else:
            parent[pv] = pu
            rank[pu] += 1

    edges.sort(key=lambda x: x[2])  # Sort by weight
    mst_edges = []
    total_weight = 0
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, w))
            total_weight += w

    print("Minimum Spanning Tree (Kruskal's):")
    for u, v, w in mst_edges:
        print(f"Edge: {u} - {v}, Weight: {w}")
    print(f"Total MST weight: {total_weight}")

    # Visualization
    G = nx.Graph()
    for u in range(num_vertices):
        G.add_node(u)
    edge_labels = {(u, v): w for u, v, w in edges}
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
    mst_edge_list = [(u, v) for u, v, _ in mst_edges]
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_edges(G, pos, edgelist=mst_edge_list, edge_color='red', width=2)
    plt.title("Kruskal's Minimum Spanning Tree (Red Edges)")
    plt.show()

def dijkstra_shortest_path():
    """Implement Dijkstra's Shortest Path algorithm with visualization."""
    graph, num_vertices, _ = get_graph_from_user()
    if graph is None:
        return
    try:
        source = int(input("Enter the source vertex: "))
        if source < 0 or source >= num_vertices:
            raise ValueError(f"Source vertex must be between 0 and {num_vertices - 1}.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    distances = [float('inf')] * num_vertices
    distances[source] = 0
    predecessors = [None] * num_vertices
    pq = [(0, source)]
    visited = set()

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        for neighbor, weight in graph[current_vertex]:
            if neighbor in visited:
                continue
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    print("\nShortest distances from source vertex", source, ":")
    for i in range(num_vertices):
        dist = distances[i] if distances[i] != float('inf') else "∞"
        print(f"Vertex {i}: Distance = {dist}")
    print("\nShortest path tree (predecessor of each vertex):")
    for i in range(num_vertices):
        pred = predecessors[i] if predecessors[i] is not None else "None"
        print(f"Vertex {i}: Predecessor = {pred}")

    # Visualization
    G = nx.Graph()
    for u in range(num_vertices):
        G.add_node(u)
    edge_labels = {}
    for u in range(num_vertices):
        for v, w in graph[u]:
            if v > u:
                G.add_edge(u, v, weight=w)
                edge_labels[(u, v)] = w
    shortest_path_edges = [(predecessors[i], i) for i in range(num_vertices) if predecessors[i] is not None]
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='red', width=2)
    node_labels = {i: f"{i}\nDist: {distances[i] if distances[i] != float('inf') else '∞'}" for i in range(num_vertices)}
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    plt.title("Dijkstra's Shortest Paths (Red Edges)")
    plt.show()

def job_scheduling():
    """Implement Job Scheduling Problem with greedy approach."""
    try:
        n = int(input("Enter the number of jobs: "))
        if n <= 0:
            raise ValueError("Number of jobs must be positive.")
        jobs = []
        print("Enter job details (format: job_id deadline profit):")
        for _ in range(n):
            jid, deadline, profit = input().split()
            deadline, profit = int(deadline), int(profit)
            if deadline <= 0 or profit < 0:
                raise ValueError("Deadline must be positive and profit non-negative.")
            jobs.append((jid, deadline, profit))
        jobs.sort(key=lambda x: x[2], reverse=True)  # Sort by profit
        max_deadline = max(job[1] for job in jobs)
        slot = [None] * max_deadline
        total_profit = 0
        scheduled_jobs = []
        for jid, deadline, profit in jobs:
            for j in range(min(deadline, max_deadline) - 1, -1, -1):
                if slot[j] is None:
                    slot[j] = jid
                    total_profit += profit
                    scheduled_jobs.append((jid, j + 1, profit))
                    break
        print("\nScheduled Jobs:")
        for jid, deadline, profit in scheduled_jobs:
            print(f"Job {jid}: Scheduled at deadline {deadline}, Profit = {profit}")
        print(f"Total Profit: {total_profit}")
    except ValueError as e:
        print(f"Error: {e}")

def minimum_spanning_tree():
    """Redirect to Prim's or Kruskal's based on user choice."""
    print("Minimum Spanning Tree can be computed using:")
    print("1. Prim's Algorithm")
    print("2. Kruskal's Algorithm")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        prim_mst()
    elif choice == "2":
        kruskal_mst()
    else:
        print("Invalid choice. Please select 1 or 2.")

def menu():
    """Display menu and get user choice."""
    print("\nGreedy Algorithms Menu:")
    print("1. Selection Sort")
    print("2. Minimum Spanning Tree")
    print("3. Single-Source Shortest Path Problem (Dijkstra's)")
    print("4. Job Scheduling Problem")
    print("5. Prim's Minimal Spanning Tree Algorithm")
    print("6. Kruskal's Minimal Spanning Tree Algorithm")
    print("7. Dijkstra's Shortest Path Algorithm")
    return input("Enter your choice (1-7): ").strip()

def main():
    """Main function with switch-case-like structure."""
    switch = {
        "1": selection_sort,
        "2": minimum_spanning_tree,
        "3": dijkstra_shortest_path,
        "4": job_scheduling,
        "5": prim_mst,
        "6": kruskal_mst,
        "7": dijkstra_shortest_path
    }
    while True:
        choice = menu()
        action = switch.get(choice)
        if action:
            try:
                action()
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("Invalid choice. Please select a number between 1 and 7.")
        if input("Run another algorithm? (yes/no): ").strip().lower() != 'yes':
            break

if __name__ == "__main__":
    main()


# In[ ]:


|


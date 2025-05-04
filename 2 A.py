#!/usr/bin/env python
# coding: utf-8

# In[2]:


import heapq
import copy

def heuristic(state, goal):
    """Calculates the Manhattan distance heuristic."""
    distance = 0
    goal_flat = [num for row in goal for num in row]
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(goal_flat.index(state[i][j]), 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    """Returns possible moves for the blank tile (0) in the 8-puzzle."""
    neighbors = []
    moves = [(-1, 0, 'Move Up'), (1, 0, 'Move Down'), (0, -1, 'Move Left'), (0, 1, 'Move Right')]

    # Find the blank tile (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                blank_i, blank_j = i, j
                break
        else:
            continue
        break

    # Generate valid moves
    for di, dj, move_name in moves:
        new_i, new_j = blank_i + di, blank_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = copy.deepcopy(state)
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            neighbors.append((new_state, move_name))
    return neighbors

def a_star(initial, goal):
    """Implements A* algorithm to solve the 8-puzzle."""
    priority_queue = []
    visited = set()
    heapq.heappush(priority_queue, (heuristic(initial, goal), initial, [], 0))  # (f, state, path, g)

    while priority_queue:
        f_score, current, path, g_score = heapq.heappop(priority_queue)
        current_tuple = tuple(tuple(row) for row in current)

        if current == goal:
            return path + [(current, 'Goal')]  # Final state

        if current_tuple in visited:
            continue

        visited.add(current_tuple)

        for new_state, move in get_neighbors(current):
            new_tuple = tuple(tuple(row) for row in new_state)
            if new_tuple not in visited:
                new_g = g_score + 1
                new_f = new_g + heuristic(new_state, goal)
                heapq.heappush(priority_queue, (new_f, new_state, path + [(new_state, move)], new_g))

    return None  # No solution found

def print_puzzle(state):
    """Prints the 8-puzzle state in a readable format."""
    for row in state:
        print(" ".join(str(num) if num != 0 else "-" for num in row))
    print()

def main():
    initial = []
    goal = []
    print("Enter initial state (3x3 grid, row-wise, use 0 for blank):")
    for _ in range(3):
        initial.append(list(map(int, input().split())))
    print("Enter goal state (3x3 grid, row-wise, use 0 for blank):")
    for _ in range(3):
        goal.append(list(map(int, input().split())))

    solution = a_star(initial, goal)

    if solution:
        print("\n Solution found! Steps:")
        for step, (state, move) in enumerate(solution):
            print(f"Step {step}: {move}")
            print_puzzle(state)
    else:
        print(" No solution found.")

if __name__ == "__main__":
    main()


# In[ ]:





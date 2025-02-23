import heapq

# A* algorithm
def astar(graph, start, goal, heuristic):
    visited = set()  # To keep track of visited nodes
    priority_queue = [(heuristic(start, goal), 0, start, [start])]  # (f, g, node, path)

    while priority_queue:
        f, g, node, path = heapq.heappop(priority_queue)  # Pop the node with the lowest f value
        if node == goal:
            return g, path  # Return the total cost (g) and the path to the goal
        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node]:  # Explore neighbors with their edge costs
                if neighbor not in visited:
                    new_g = g + cost  # Update the cost to reach the neighbor
                    new_f = new_g + heuristic(neighbor, goal)  # Calculate f = g + h
                    heapq.heappush(priority_queue, (new_f, new_g, neighbor, path + [neighbor]))
    return None


# Define the graph as an adjacency list with edge costs
# Graph structure:
#
#        A (h=6)
#       / \
#   1 /     \ 4
#    B(h=4)  C(h=5)
#   / \        \
# 2/   \5      3\
# D(h=2) E(h=3)  F(h=0)
#/
#F(h=0)
graph = {
    'A': [('B', 1), ('C', 4)],  # Node A has neighbors B (cost 1) and C (cost 4)
    'B': [('D', 2), ('E', 5)],  # Node B has neighbors D (cost 2) and E (cost 5)
    'C': [('F', 3)],            # Node C has neighbor F (cost 3)
    'D': [('F', 1)],            # Node D has neighbor F (cost 1)
    'E': [],                    # Node E has no neighbors
    'F': []                     # Node F has no neighbors
}

# Define the heuristic function as a dictionary
heuristic_values = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 3,
    'F': 0  # Goal node
}

# Heuristic function
def heuristic(node, goal):
    return heuristic_values[node]


# Run A* starting from node 'A', searching for goal node 'F'
print("Running A*:")
result = astar(graph, 'A', 'F', heuristic)

if result:
    cost, path = result
    print(f"Lowest Cost: {cost}")
    print(f"Path: {' -> '.join(path)}")
else:
    print("No path found.")
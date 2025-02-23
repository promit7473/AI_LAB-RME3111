import heapq

def ucs(graph, start, goal):
    visited = set()  # To keep track of visited nodes
    priority_queue = [(0, start, [start])]  # (cost, node, path)

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)  # Pop the least costly path
        if node == goal:
            return cost, path  # Return the total cost and the path to the goal
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node]:  # Explore neighbors with their edge costs
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [neighbor]))
    return None


# Define the graph as an adjacency list with edge costs
# Graph structure:
#
#               A
#             /   \
#        1/       \4
#       B         C
#      /  \         \
# 2/    5\         \3
# D      E         F
#
graph = {
    'A': [('B', 1), ('C', 4)],  # Node A has neighbors B (cost 1) and C (cost 4)
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5)],
    'F': [('C', 3)]
}

# Run UCS starting from node 'A', searching for goal node 'F'
print("Running UCS:")
result = ucs(graph, 'A', 'E')

if result:
    cost, path = result
    print(f"Lowest Cost: {cost}")
    print(f"Path: {' -> '.join(path)}")
else:
    print("No path found.")
from collections import deque

# DFS function to return traversal path
def dfs_traversal(graph, start_node, goal_node=None):
    visited = set()
    stack = [start_node]  # Using list as a stack
    traversal_path = []   # To store the traversal order

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            traversal_path.append(current_node)
            visited.add(current_node)
            print(current_node, end=" ")
            # Check if we've found the goal node
            if current_node == goal_node:
                print(f"\nGoal node {goal_node} found!")
                return traversal_path
        # Adding neighbors to the stack (reverse order to maintain left-to-right exploration)
        for neighbor in reversed(graph.get(current_node, [])):
            if neighbor not in visited:
                stack.append(neighbor)

    print(f"\nGoal node {goal_node} not found.")
    return traversal_path


# BFS function to find the shortest path
def bfs_shortest_path(graph, start_node, goal_node):
    visited = set()  # To keep track of visited nodes
    queue = deque([(start_node, [start_node])])  # Queue stores tuples of (current_node, path_to_current_node)

    while queue:
        current_node, path = queue.popleft()  # Dequeue the first element
        if current_node == goal_node:
            print(f"\nShortest path to goal node {goal_node}: {' -> '.join(path)}")
            return path  # Return the shortest path
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))  # Enqueue the neighbor with updated path

    print(f"\nNo path found to goal node {goal_node}.")
    return None


# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Run DFS starting from node 'A', searching for goal node 'F'
print("DFS Traversal Path:")
dfs_path = dfs_traversal(graph, 'A', 'F')

# Print the DFS traversal path
print(f"\nDFS Traversal Path: {dfs_path}")

# Run BFS starting from node 'A', searching for goal node 'F'
print("\nFinding shortest path using BFS:")
bfs_path = bfs_shortest_path(graph, 'A', 'E')

# Print the BFS shortest path
if bfs_path:
    print(f"BFS Shortest Path: {bfs_path}")
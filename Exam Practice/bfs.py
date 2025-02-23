from collections import deque

# BFS function to return traversal path and shortest path
def bfs(graph, start_node, goal_node=None):
    visited = set()  # To keep track of visited nodes
    queue = deque([(start_node, [start_node])])  # Queue stores tuples of (current_node, path_to_current_node)
    traversal_path = []  # To store the traversal order

    while queue:
        current_node, path = queue.popleft()
        if current_node not in visited:
            # Add the current node to the traversal path
            traversal_path.append(current_node)
            visited.add(current_node)

            # Check if we've found the goal node
            if current_node == goal_node:
                print(f"\nGoal node {goal_node} found!")
                print(f"Traversal Path: {' -> '.join(traversal_path)}")
                print(f"Shortest Path: {' -> '.join(path)}")
                return traversal_path, path

            # Add neighbors to the queue with updated paths
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    print("\nBFS Traversal Completed.")
    print(f"Traversal Path: {' -> '.join(traversal_path)}")
    if goal_node:
        print(f"No path found to goal node {goal_node}.")
    return traversal_path, None


# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Run BFS starting from node 'A', searching for goal node 'F'
print("BFS Traversal (Starting from A):")
traversal_path, shortest_path = bfs(graph, 'A', 'F')

# Print results
if shortest_path:
    print(f"\nFinal Traversal Path: {traversal_path}")
    print(f"Final Shortest Path: {shortest_path}")
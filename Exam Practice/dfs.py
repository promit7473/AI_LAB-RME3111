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
traversal_path = dfs_traversal(graph, 'A', 'F')

# Print the traversal path
print(f"\nTraversal Path: {traversal_path}")
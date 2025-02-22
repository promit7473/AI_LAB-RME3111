# dfs.py

from stack import Stack  # Importing custom Stack class

def dfs(graph, start_node):
    visited = set()
    stack = Stack(100)  # Initializing a stack with size 100

    stack.push(start_node)

    while not stack.is_empty():  # While the stack is not empty
        current_node = stack.pop()

        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)

        # Adding neighbors to the stack
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                stack.push(neighbor)

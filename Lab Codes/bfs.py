# bfs.py

from queue import Queue

def bfs(graph, start_node):
    visited = set()
    q = Queue(len(graph))  # Initializing custom queue with size
    q.enqueue(start_node)
    visited.add(start_node)

    while q.head != -1:  # While the queue is not empty
        current_node = q.dequeue()

        if current_node is None:
            continue  # Skipping if no more nodes

        print(current_node, end=" ")

        for neighbor in graph.get(current_node, []):  # Ensuring graph has the node
            if neighbor not in visited:
                q.enqueue(neighbor)
                visited.add(neighbor)

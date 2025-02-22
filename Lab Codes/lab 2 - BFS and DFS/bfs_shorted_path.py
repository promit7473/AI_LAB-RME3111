from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)


        for neighbor in graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)


test_graph = {
    '9': ['11', '4'],
    '4': ['3', '1'],
    '7': ['2', '5'],
    '8': ['6'],
    '11': ['7', '8']
}

path = bfs_shortest_path(test_graph, '9', '7')
print(path)

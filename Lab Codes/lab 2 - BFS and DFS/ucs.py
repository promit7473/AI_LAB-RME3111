import heapq

def uniform_cost_search(graph, start, goal):
    visited = set()
    priority_queue = [(0, start, [start])]

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return cost, path

        for neighbour, weight in graph[node].items():
            #print(neighbour, weight)
            if neighbour not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbour, path + [neighbour]))

    return None

test_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'E': 1},
    'D': {'B': 2, 'G': 3},
    'E': {'B': 5, 'G': 1, 'C': 4},
    'G': {'D': 3, 'E': 1}
}

print(uniform_cost_search(test_graph, 'A', 'G'))



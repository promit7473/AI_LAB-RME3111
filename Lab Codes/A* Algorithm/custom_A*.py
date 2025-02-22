# Custom heap implementation
def reheapUp(heap, index):
    parent_index = (index - 1) // 2
    if index > 0 and heap[index] < heap[parent_index]:  # Min-heap property
        heap[index], heap[parent_index] = heap[parent_index], heap[index] #I will just swap
        reheapUp(heap, parent_index)


def enqueue(heap, value):
    heap.append(value)
    reheapUp(heap, len(heap) - 1)


def reheapDown(heap, index):
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    current = index

    if left_child < len(heap) and heap[left_child] < heap[current]:  # Min-heap property
        current = left_child

    if right_child < len(heap) and heap[right_child] < heap[current]:  # Min-heap property
        current = right_child

    if current != index:
        heap[index], heap[current] = heap[current], heap[index] #swap
        reheapDown(heap, current)


def dequeue(heap):
    min_value = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    reheapDown(heap, 0)
    return min_value



def astar(graph, heuristic, start, goal):

    priority = []
    #(f_value, current_cost, node, path)
    enqueue(priority, (0+heuristic[start],0, start, [start]))


    #visited nodes
    explored = set()


    while priority:
        # extracting the node with lowest f_value
        f_value, current_cost, current_node, path = dequeue(priority)


        if current_node == goal:
            return path, current_cost

        if current_node in explored:
            continue

        if current_node not in explored:
            explored.add(current_node)

        for neighbor, step_cost in graph[current_node]:
            if neighbor not in explored:
                new_cost = current_cost + step_cost
                f_value = new_cost + heuristic[neighbor]
                new_path = path + [neighbor]
                enqueue(priority,(f_value, new_cost, neighbor, new_path))

    return None


# Example graph and heuristics
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('E', 1), ('D', 3)],
    'C': [('A', 3), ('F', 5)],
    'D': [('B', 3), ('G', 2)],
    'E': [('B', 1), ('G', 2)],
    'F': [('C', 5), ('G', 5)],
    'G': [('F', 5), ('E', 2)]
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0
}

# Running the A* search
start_node = 'A'
goal_node = 'G'
cost, path = astar(graph, heuristics, start_node, goal_node)

print("Total cost from A to G:", cost)
print("Path from A to G:", path)
from queue import PriorityQueue

def astar(graph, heuristic, start, goal):

    priority = PriorityQueue()
    #(f_value, current_cost, node, path)
    priority.put((0+heuristic[start],0, start, [start]))


    #visited nodes
    explored = set()


    while not priority.empty():
        # extracting the node with lowest f_value
        f_value, current_cost, current_node, path = priority.get()


        if current_node == goal:
            return path, current_cost

        if current_node in explored:
            continue

        if current_node not in explored:
            explored.add(current_node)

        for neighbor, step_cost in graph[current_node].items():
            if neighbor not in explored:
                new_cost = current_cost + step_cost
                f_value = new_cost + heuristic[neighbor]
                new_path = path + [neighbor]
                priority.put((f_value, new_cost, neighbor, new_path))

    return None


def main():

    given_graph = {
            'A': {'B': 1, 'C': 5},
            'B': {'D': 3, 'E': 1},
            'C': {'A': 3, 'F': 3},
            'D': {'B': 3, 'G': 0},
            'E': {'B': 1, 'G': 2},
            'F': {'C': 3, 'G': 5},
            'G': {'D': 2, 'E': 2, 'F':5}
    }

    given_heuristic = {
        'A': 7,
        'B': 6,
        'C': 5,
        'D': 3,
        'E': 2,
        'F': 4,
        'G': 0
    }

    given_start = 'A'
    given_goal = 'G'
    path, cost = astar(given_graph, given_heuristic, given_start, given_goal)

    if path:
        print(f"Path found: {' -> '.join(path)}")
        print(f"Cost: {cost}")


if __name__ == '__main__':
    main()
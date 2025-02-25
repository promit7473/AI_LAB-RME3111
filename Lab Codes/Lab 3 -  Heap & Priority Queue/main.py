# main.py

def read_graph_from_file(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            nodes = line.strip().split()
            graph[nodes[0]] = nodes[1:]
    return graph

if __name__ == "__main__":
    graph = read_graph_from_file("graph.txt")
    print(graph)


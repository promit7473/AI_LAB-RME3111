# main.py

from bfs import bfs
#from dfs import dfs
#from heap_down import reheap_down


def read_graph_from_file(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            nodes = line.strip().split()
            graph[nodes[0]] = nodes[1:]
    return graph

if __name__ == "__main__":
    graph = read_graph_from_file("graph.txt")

    print("BFS Traversal:")
    bfs(graph, 9)  # Starting node 'A'
    #
    # print("\nDFS Traversal:")
    # dfs(graph, 'A')  # Starting node 'A'
    print("\n")
    print("graph", graph)
    print(len(graph))




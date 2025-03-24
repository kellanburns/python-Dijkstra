# Kellan Burns, python-Dijkstra project

from Classes.MinHeap import MinHeap

def reconstructPath(parents: [int], target: int) -> str:
    path = []

    while target != -1:
        path.insert(0, str(target))
        target = parents[target]

    return " -> ".join(path)

def printResults(distances: [int], parents: [int], source: int) -> None:
    print(f"Shortest path from:")

    for i in range(len(distances)):
        if (distances[i] == float('inf')):
            print(f"\tNode {source} to node {i}:".ljust(20), f"Node {i} unreachable from source")
        else:
            path = reconstructPath(parents, i)
            print(f"\tNode {source} to node {i}:".ljust(20), f"({path})".ljust(20), f"distance: {distances[i]}")

def dijkstra(graph: [], source: int) -> None:
    n = len(graph)
    distances = [float('inf')] * n
    parents = [-1] * n
    visited = [False] * n
    heap = MinHeap(n)

    heap.insert(source, 0) # insert source
    distances[source] = 0
    heap.decreaseKey(source, 0)

    while not (heap.isEmpty()):
        u = heap.extractMin()
        if (visited[u]):
            continue
        visited[u] = True

        current = graph[u].get_head()
        while (current):
            edge = current.get_edge()
            v = int(edge.get_destination())
            weight = int(edge.get_weight())

            if(not visited[v] and distances[u] + weight < distances[v]):
                distances[v] = distances[u] + weight
                parents[v] = u
                if heap.position[v] == -1:
                    heap.insert(v, distances[v])
                else:
                    heap.decreaseKey(v, distances[v])

            current = current.get_next()

    printResults(distances, parents, source)
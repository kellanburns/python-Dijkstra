# Kellan Burns, python-Dijkstra project
from Classes.LinkedList import LinkedList
from Classes.MinHeap import MinHeap

def reconstructPath(parents: [int], target: int) -> str:
    path = []
    while target != -1:
        path.insert(0, str(target))
        target = parents[target]
    return ",".join(path)

def printResults(distances: [int], parents: [int], source: int) -> None:
    for i in range(len(distances)):
        if (distances[i] == float('inf')):
            print(f"[{i}] unreachable")
        else:
            path = reconstructPath(parents, i)
            print(f"[{i}] shortest path: {path} shortest distance: {distances[i]}")

def dijkstra(graph: [], source: int) -> None:
    n = len(graph)
    distances = [float('inf')] * n
    parents = [-1] * n
    visited = [False] * n
    heap = MinHeap(n)

    distances[source] = 0
    heap.decreaseKey(source, 0)

    while not (heap.isEmpty()):
        u = heap.extractMin()
        if (visited[u]):
            continue
        visited[u] = True

        current = graph[u].head
        while (current):
            edge = current.edge
            v = int(edge.destination)
            weight = int(edge.weight)

            if((not visited[v]) and (distances[u] + weight < distances[v])):
                distances[v] = distances[u] + weight
                parents[v] = u
                heap.decreaseKey(v, distances[v])

            current = current.next

    printResults(distances, parents, source)
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

def dijkstra(graph: [LinkedList], source: int) -> None:
    n = graph.length
    distances = [int]
    parents = [int]
    visited = [bool]
    heap = MinHeap(n)

    for i in range(n):
        distances[i] = float('inf')
        parents[i] = -1
        heap.insert(i, distances[i])

    distances[source] = 0
    heap.decreaseKey(source, 0)

    while heap:
        u = heap.extractMin()
        if (visited[u]):
            continue
        visited[u] = True

        current = graph[u].head
        while (current):
            edge = current.edge
            v = edge.destination
            weight = edge.weight

            if(not visited[v] and distances[u] + weight < distances[v]):
                distances[v] = distances[u] + weight
                parents[v] = u
                heap.decreaseKey(v, distances[v])

            current = current.next

    printResults(distances, parents, source)
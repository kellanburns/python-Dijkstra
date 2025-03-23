# Kellan Burns, python-Dijkstra project

from Classes.LinkedList import LinkedList

def lineCounter(fileName: str) -> int:
    with open(fileName, 'r') as reader:
        return sum(1 for line in reader if (line.strip()))

def graphReader(fileName: str) -> list[LinkedList]:
    lineCount = lineCounter(fileName)
    graph = [LinkedList() for _ in range(lineCount)]

    with open(fileName, 'r') as reader:
        for line in reader:
            parts = line.strip().split(":")
            vertex = int(parts[0].strip())
            if ((len(parts) > 1) and (parts[1].strip())):
                neighbors = parts[1].strip().split(";")
                for neighbor in neighbors:
                    edge_parts = neighbor.strip().split(",")
                    destination = edge_parts[0].strip()
                    weight = edge_parts[1].strip()
                    graph[vertex].add(destination, weight)



    return graph

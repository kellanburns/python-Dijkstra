# Kellan Burns, python-Dijkstra project

from Classes.LinkedList import LinkedList

def lineCounter(fileName: str) -> int:
    with open(fileName, 'r') as reader:
        return sum(1 for line in reader if (line.strip()))

def graphReader(fileName: str) -> list[LinkedList]:
    lineCount = int(lineCounter(fileName))
    graph = [LinkedList() for _ in range(lineCount)]

    with open(fileName, 'r') as reader:
        for line_num, line in enumerate(reader):
            parts = line.strip().split(":")
            vertex = int(parts[0].strip())

            if ((len(parts) > 1) and (parts[1].strip())):
                neighbors = parts[1].strip().split(";")

                for neighbor in neighbors:
                    edge_parts = neighbor.strip().split(",")
                    destination = int(edge_parts[0].strip())
                    weight = int(edge_parts[1].strip())

                    if ((destination < 0) or (destination > lineCount)):
                        raise ValueError(f"Error: GraphReader.graphReader: bad destination '{edge_parts[0]}'")

                    graph[vertex].add(destination, weight)

    return graph

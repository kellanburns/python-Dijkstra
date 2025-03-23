# Kellan Burns, python-Dijkstra project

import sys

from Utilities.Dijkstra import dijkstra
from Utilities.GraphReader import graphReader


def main():
    print("Test line")

    if (len(sys.argv) != 3):
        raise ValueError("Usage: python main.py <input_file> <source_vertex>")

    inputFileName = sys.argv[1]
    source = int(sys.argv[2])
    graph = graphReader(inputFileName)
    dijkstra(graph, source)

if __name__ == "__main__":
    main()
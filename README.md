# python-Dijkstra
Python implementation of Dijkstra's algorithm, which finds the shortest path from a point to all other points in a weighted graph. The program uses custom Min-Heap and Linked-List/ Adjacency-List classes to represent the graph, and outputs the shortest path from the source to the rest of the connected nodes.

python-Dijkstra:

| Directory       | File             | Description                                                             |
|----------------|------------------|-------------------------------------------------------------------------|
| `Classes/`      | `LinkedList.py`  | Linked-List class with nested `Node` and `Edge` classes and functions. |
|                | `MinHeap.py`     | Min-Heap class and associated functions.                                |
| `Utilities/`    | `Dijkstra.py`    | Dijkstra's algorithm implementation with output functions.             |
|                | `GraphReader.py` | File input functions.                                                   |
| *(root)*        | `main.py`        | Program entry point (CLI runner).                                      |

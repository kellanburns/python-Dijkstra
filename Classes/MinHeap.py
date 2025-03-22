class MinHeap(object):
    def __init__(self, capacity: int):
        self.heap = [0] * capacity
        self.key = [0] * capacity
        self.position = [-1] * capacity
        self.size = 0


    def swap(self, i: int, j: int) -> None:
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp
        self.position[self.heap[i]] = i
        self.position[self.heap[j]] = j

    def bubbleUp(self, index: int):
        while index > 0:
            parent = (index - 1) / 2
            if (self.key[self.heap[index]] < self.key[parent]):
                self.swap(index, parent)
            else:
                break

    def bubbleDown(self, index: int) -> None:
        left, right, smallest = -1
        while (index < self.size):
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if (left < self.size and self.key[self.heap[left]] < self.key[self.heap[smallest]]):
                smallest = left
            if (right < self.size and self.key[self.heap[right]] < self.key[self.heap[smallest]]):
                smallest = right
            if (smallest != index):
                self.swap(index, smallest)
                index = smallest
            else:
                break

    def insert(self, vertex: int, k: int) -> None:
        self.position[vertex] = self.size
        self.heap[self.size] = vertex
        self.key[vertex] = k
        self.size = self.size + 1
        self.bubbleUp(self.size - 1)

    def extractMin(self) -> int:
        minVertex = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.position[minVertex] = -1
        self.position[self.heap[0]] = 0
        self.size = self.size - 1
        self.bubbleDown(0)
        return minVertex

    def decreaseKey(self, vertex: int, newKey: int) -> None:
        index = self.position[vertex]
        self.key[vertex] = newKey
        self.bubbleUp(index)

    def isEmpty(self) -> bool:
        return self.size == 0

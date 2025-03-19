
class LinkedList:
    class __Edge:
        # Edge Constructor
        def __init__(self, destination: int, weight: int):
            self.destination = destination
            self.weight = weight

    class __Node:
        # Node Constructor
        def __init__(self, edge: int = -1, next: "LinkedList.__Node" = None):
            self.edge = edge
            self.next = next

    # LinkedList Constructor
    def __init__(self, head=None):
        self.head = head

    # LinkedList add() method
    def add(self, destination: int, weight: int) -> None:
        newNode = self.LinkedList.__Node(LinkedList.__Edge(destination, weight))

        if self.head is None:
            self.head = newNode
        else:
            temp =  self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode


class LinkedList(object):
    class __Edge:
        # Edge Constructor
        def __init__(self, destination: int, weight: int):
            self.destination = destination
            self.weight = weight

        def get_destination(self) -> int:
            # print("Function: LinkedList.Edge.get_destination()")

            return self.destination

        def get_weight(self) -> int:
            # print("Function: LinkedList.Edge.get_weight()")

            return self.weight

        def set_destination(self, destination: int) -> None:
            # print("Function: LinkedList.Edge.set_destination()")

            self.destination = destination

        def set_weight(self, weight: int) -> None:
            # print("Function: LinkedList.Edge.set_weight()")

            self.weight = weight

    class __Node:
        # Node Constructor
        def __init__(self, edge: int):
            self.edge = edge
            self.next = None

        def get_edge(self) -> int:
            # print("Function: LinkedList.Node.get_edge()")

            return self.edge

        def get_next(self) -> "LinkedList.__Node":
            return self.next

        def set_edge(self, edge: int) -> None:
            self.edge = edge

        def set_next(self, next: "LinkedList.__Node") -> None:
            self.next = next

    # LinkedList Constructor
    def __init__(self, head=None):
        self.head = head

    def get_head(self) -> "LinkedList.__Node":
        return self.head

    def set_head(self, head: "LinkedList") -> None:
        self.head = head

    # LinkedList add() method
    def add(self, destination: int, weight: int) -> None:
        newNode = LinkedList.__Node(LinkedList.__Edge(destination, weight))

        if self.head is None:
            self.head = newNode
        else:
            temp =  self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

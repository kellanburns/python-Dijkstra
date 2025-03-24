
class LinkedList(object):
    class __Edge:
        def __init__(self, destination: int, weight: int):
            self.__destination = destination
            self.__weight = weight

        def get_destination(self) -> int:
            return self.__destination

        def get_weight(self) -> int:
            return self.__weight

        def set_destination(self, destination: int) -> None:
            self.__destination = destination

        def set_weight(self, weight: int) -> None:
            self.__weight = weight

    class __Node:
        def __init__(self, edge: int):
            self.__edge = edge
            self.__next = None

        def get_edge(self) -> int:
            return self.__edge

        def get_next(self) -> "LinkedList.__Node":
            return self.__next

        def set_edge(self, edge: int) -> None:
            self.__edge = edge

        def set_next(self, next: "LinkedList.__Node") -> None:
            self.__next = next

    def __init__(self, head=None):
        self.__head = head

    def get_head(self) -> "LinkedList.__Node":
        return self.__head

    def set_head(self, head: "LinkedList") -> None:
        self.__head = head

    def add(self, destination: int, weight: int) -> None:
        newNode = LinkedList.__Node(LinkedList.__Edge(destination, weight))

        if self.__head is None:
            self.__head = newNode
        else:
            temp = self.__head
            while temp.get_next() is not None:
                temp = temp.get_next()
            temp.set_next(newNode)

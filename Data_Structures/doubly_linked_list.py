from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.prev: Node | None = None
        self.next: Node | None = None

    def __repr__(self):
        return f"<Node data: {self.data}>"


class Doubly_Linked_List:
    def __init__(self):
        self.head: Node | None = None

    def __repr__(self):
        if not self.head:
            return "Empty List"

        current: Node | None = self.head
        _list: list[str] = []

        while current:
            _list.append(str(current.data))
            current = current.next

        return " -> ".join(_list)

    def append(self, data: Any) -> None:
        new_node: Node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current: Node | None = self.head

        while current.next:
            current = current.next

        current.next = new_node
        current.prev = current

    def prepend(self, data: Any) -> None:
        new_node: Node = Node(data)

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    def insert(self, data: Any, index: int) -> None:
        new_node: Node = Node(data)

        if index < 0:
            raise IndexError("Index cannot be a negative value!")

        if index == 0:
            self.prepend(data)
            return

        current: Node | None = self.head
        pos: int = index

        while current and pos > 1:
            current = current.next
            pos -= 1

        if not current:
            raise IndexError("Index out of range")

        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node

        current.next = new_node

    def size(self) -> int:
        current: Node | None = self.head
        count: int = 0

        while current:
            count += 1
            current = current.next

        return count

    def search(self, key: Any) -> int:
        """
        Search for the index of a node that contains the key.
        Return the index if success to find,
        but raise an ValueError when the list is empty
        or Key Error if key not found.
        """

        current: Node | None = self.head

        if not current:
            raise ValueError("List is empty")

        pos: int = 0

        while current:
            if current.data == key:
                return pos

            current = current.next
            pos += 1

        raise KeyError("Key not found!")

    def remove(self, key: any) -> None:
        if key == self.head.data:
            self.head = self.head.next

        current: Node | None = self.head
        prev: Node = None

        while current and key != self.head.data:
            prev = current
            current = current.next

        if not current:
            raise KeyError(f"The key {key} is not found!")

        if current.next:
            current.next.prev = prev.next

        prev.next = current.next


def main() -> None:
    print("Doubly Linked List")


if __name__ == "__main__":
    main()

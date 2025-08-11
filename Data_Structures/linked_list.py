from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next_node: Node | None = None

    def __repr__(self):
        return f"<Node data: {self.data}>"


class Linked_List:
    def __init__(self):
        self.head: Node | None = None

    def __repr__(self):
        current: Node | None = self.head

        if not current:
            return "None"

        _list: list[str] = []
        while current:
            _list.append(str(current.data))
            current = current.next_node

        return " -> ".join(_list)

    def append(self, data: Any) -> None:
        new_node: Node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current: Node | None = self.head
        while current.next_node:
            current = current.next_node

        current.next_node = new_node

    def prepend(self, data: Any) -> None:
        new_node: Node = Node(data)

        new_node.next_node = self.head
        self.head = new_node

    def size(self) -> int:
        current: Node | None = self.head
        count: int = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def delete_head(self) -> None:
        if self.is_empty():
            return

        self.head = self.head.next_node

    def delete_tail(self) -> None:
        if self.is_empty():
            return

        if not self.head.next_node:
            self.head = None
            return

        current: Node | None = self.head
        while current.next_node and current.next_node.next_node:
            current = current.next_node

        current.next_node = None

    def search(self, key: Any) -> Node:
        """
        Search for the first node containing data that matches the key.
        Return the node or "None" if not found.
        """

        current: Node | None = self.head

        while current:
            if current.data == key:
                return current

            current = current.next_node

        return None

    def insert(self, data: Any, index: int) -> None:
        """
        Inserts a new node containing data at index position.
        Insertion takes O(1) time but finding the node at the Insertion
        point takes O(n) time
        """

        if index < 0:
            raise IndexError("Negative index are not supported!")

        if index == 0:
            self.prepend(data)
            return

        new_node: Node = Node(data)
        pos: int = index
        current: Node | None = self.head

        while pos > 1 and current:
            current = current.next_node
            pos -= 1

        if not current:
            raise IndexError("Index out of bounds")

        new_node.next_node = current.next_node
        current.next_node = new_node

    def remove(self, key: Any) -> None:
        if not self.is_empty():
            return

        current: Node | None = self.head
        prev: Node | None = None

        if current.data == key:
            self.head = self.head.next_node
            return

        while current and current.data != key:
            prev = current
            current = current.next_node

        if not current:
            raise ValueError(f"{key} not found in the list")

        prev.next_node = current.next_node

    def is_empty(self) -> bool:
        if not self.head:
            print("Linked list is empty!")
            return True

        return False


def main() -> None:
    print("Linked_List")


if __name__ == "__main__":
    main()

from typing import Any


class Min_Heap:
    def __init__(self):
        self.heap: list[Any] = []

    def __repr__(self):
        return f"{self.heap}"

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def left(self, i: int) -> int:
        return 2 * i + 1

    def right(self, i: int) -> int:
        return 2 * i + 2

    def insert(self, value: Any) -> None:
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i: int) -> None:
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            temp: Any = self.heap[i]

            self.heap[i] = self.heap[self.parent(i)]
            self.heap[self.parent(i)] = temp

            i = self.parent(i)

    def peek(self) -> Any:
        return self.heap[0] if self.heap else None

    def extract_min(self) -> Any | None:
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root: Any = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return root

    def heapify_down(self, i: int) -> None:
        smallest: int = i
        left: int = self.left(i)
        right: int = self.right(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            temp: Any = self.heap[i]
            self.heap[i] = self.heap[smallest]
            self.heap[smallest] = temp
            self.heapify_down(smallest)

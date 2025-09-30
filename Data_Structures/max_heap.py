from typing import Any
import m_heap


class Max_Heap:
    def __init__(self):
        self.heap: list[Any] = []

    def __repr__(self):
        return f"{self.heap}"

    def insert(self, value: Any) -> None:
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i: int) -> None:
        while i > 0:
            parent: int = m_heap.parent(i)

            if self.heap[i] < self.heap[parent]:
                break

            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def extract_max(self) -> Any | None:
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root: Any = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self, i: int) -> None:
        largest: int = i
        left: int = m_heap.left(i)
        right: int = m_heap.right(i)

        heap_len: int = len(self.heap)

        if left < heap_len and self.heap[left] > self.heap[largest]:
            largest = left
        if right < heap_len and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify_down(largest)


if __name__ == "__main__":
    print("Max Heap Implementation")

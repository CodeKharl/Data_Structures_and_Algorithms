from typing import Any
import m_heap


class Min_Heap:
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

            if self.heap[i] >= self.heap[parent]:
                break

            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

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
        left: int = m_heap.left(i)
        right: int = m_heap.right(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            temp: Any = self.heap[i]
            self.heap[i] = self.heap[smallest]
            self.heap[smallest] = temp
            self.heapify_down(smallest)


if __name__ == "__main__":
    print("Min Heap Implementation")

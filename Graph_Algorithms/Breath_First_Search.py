class Queue[T]:
    def __init__(self, start: T | None = None):
        self.__queue: list[T] = list()
        self.__count: int = 0

        if start:
            self.put(start)

    def put(self, data: T) -> None:
        self.__queue.append(data)
        self.__count += 1

    def pop(self) -> T:
        if not self.is_empty():
            first_value: T = self.__queue[0]
            self.__queue = self.__queue[1:]
            self.__count -= 1

            return first_value

        raise IndexError("The queue is empty")

    def is_empty(self) -> bool:
        return self.__count == 0


def bfs(graph: dict[str, list[str]], start: str):
    visited: set[str] = {start}
    queue: Queue[str] = Queue(start)

    while not queue.is_empty():
        node: str | None = queue.pop()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put(neighbor)


if __name__ == "__main__":
    graph: dict[str, list[str]] = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }

    bfs(graph, 'A')

from collections import deque


def bfs(graph: dict[str, list[str]], start: str):
    visited: set[str] = {start}
    queue: deque[str] = deque([start])

    while queue:
        node: str | None = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


if __name__ == "__main__":
    graph: dict[str, list[str]] = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B"],
        "F": ["C"],
    }

    bfs(graph, "A")

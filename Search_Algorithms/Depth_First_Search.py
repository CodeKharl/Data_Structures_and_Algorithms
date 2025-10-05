# Recursive DFS Implementation
def dfs_recursive(
        graph: dict[str, list[str]],
        start: str,
        visited: set[str] | None = None
) -> None:
    if not visited:
        visited = set()

    print(start, end=" ")
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


# Iterative DFS Implementation
def dfs_iterate(graph: dict[str, list[str]], start: str) -> None:
    visited: set[str] = set()
    stack: list[str] = list(start)

    while stack:
        node: str = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            stack.extend(reversed(graph[node]))


if __name__ == '__main__':
    graph: dict[str, list[str]] = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }

    start: str = 'A'
    dfs_recursive(graph, start)
    print(" ")
    dfs_iterate(graph, start)

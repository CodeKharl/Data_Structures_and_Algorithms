from typing import Any


def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


def parent(i: int) -> int:
    return (i - 1) // 2


def peek(heap: list[Any]) -> Any | None:
    return heap[0] if heap else None

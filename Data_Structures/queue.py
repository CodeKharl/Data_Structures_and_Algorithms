from typing import Any


class Queue:
    def __init__(self):
        self.__queue: list[Any] = []

    def __repr__(self):
        return f"{self.__queue}"

    def put(self, val: Any) -> None:
        self.__queue.append(val)

    def pop(self) -> Any | None:
        if not self.__queue:
            return None

        first_value: Any = self.__queue[0]
        self.__queue = self.__queue[1:]

        return first_value

    def peek(self) -> Any | None:
        return self.__queue[0] if self.__queue else None

    def is_empty(self) -> bool:
        return not self.__queue


if __name__ == "__main__":
    print("Queue Implementation")

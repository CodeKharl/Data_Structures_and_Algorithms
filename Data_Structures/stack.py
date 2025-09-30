from typing import Any


class Stack:
    def __init__(self):
        self.__stack: list[Any] = []

    def __repr__(self):
        return f"{self.__stack}"

    def put(self, val: Any) -> None:
        self.__stack.append(val)

    def pop(self) -> Any | None:
        return self.__stack.pop() if self.__stack else None

    def peek(self) -> Any | None:
        return self.__stack[-1] if self.__stack else None

    def is_empty(self) -> bool:
        return not self.__stack


if __name__ == "__main__":
    print("Stack Implementation")

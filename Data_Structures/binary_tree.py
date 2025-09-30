from typing import Any


class Node:
    def __init__(self, data: Any):
        self.__data: Any = data
        self.__left: Node | None = None
        self.__right: Node | None = None

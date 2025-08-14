from typing import TypeVar, Generic

V = TypeVar("V")
K = TypeVar("K")


class Hash_Table(Generic[K, V]):
    def __init__(self, size: int = 10):
        self.def_size: int = size
        self.table: list[list[tuple[K, V]]] = [[] for _ in range(size)]

    def __repr__(self):
        temp_str: str = str()

        for i, bucket in enumerate(self.table):
            temp_str += str(bucket)

        return temp_str

    def _hash(self, key: K) -> int:
        return hash(key) % self.def_size

    def insert(self, key: K, val: V) -> None:
        index: int = self._hash(key)

        for counter, (K, V) in enumerate(self.table[index]):
            if K == key:
                self.table[index][counter] = (key, val)
                return

        self.table[index].append((key, val))

    def remove(self, key: K) -> None:
        index: int = self._hash(key)

        for counter, (K, V) in enumerate(self.table[index]):
            if K == key:
                self.table[index].pop(counter)
                return

    def get(self, key: K) -> V | None:
        index: int = self._hash(key)

        for K, V in self.table[index]:
            if K == key:
                return V

        return None

    def size(self) -> int:
        return sum(len(bucket) for bucket in self.table)

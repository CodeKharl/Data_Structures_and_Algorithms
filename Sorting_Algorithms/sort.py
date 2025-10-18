from abc import ABC, abstractmethod


class Sort(ABC):
    """Abstract base class -> sorting"""

    @abstractmethod
    def sort(self, arr: list[int]) -> None:
        """Sort list of values"""
        pass

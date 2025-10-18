from .bubble_sort import BubbleSort
from .insertion_sort import InsertionSort
from .selection_sort import SelectionSort
from .sort import Sort


def run_sort(sort_type: Sort) -> None:
    """Run a demo within the sorting algorithms"""

    arr: list[int] = [1, 6, 3, 2]
    sort: Sort = sort_type
    sort.sort(arr)

    print(f"{sort} = {arr}")


if __name__ == "__main__":
    run_sort(BubbleSort())
    run_sort(InsertionSort())
    run_sort(SelectionSort())

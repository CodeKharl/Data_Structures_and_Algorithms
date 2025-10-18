from typing import Callable


def bubble_sort(arr: list[int], comparable: Callable[[list[int], int], bool]) -> None:
    arr_len: int = len(arr)

    for i in range(arr_len):
        swapped: bool = False

        for j in range(1, arr_len - i):
            if comparable(arr, j):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True

        if not swapped:
            break


def increment(arr: list[int], j: int) -> bool:
    return arr[j] < arr[j - 1]


def main():
    arr: list[int] = [7, 8, 3, 5, 1]
    bubble_sort(arr, increment)

    print(arr)


if __name__ == "__main__":
    main()

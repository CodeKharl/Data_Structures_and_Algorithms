def bubble_sort(arr: list[int]) -> None:
    arr_len: int = len(arr)

    for _ in range(arr_len):
        for j in range(1, arr_len):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


if __name__ == "__main__":
    arr: list[int] = [5, 4, 3, 2, 1]
    bubble_sort(arr)

    print(arr)

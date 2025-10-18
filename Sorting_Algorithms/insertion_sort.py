def insertion_sort(arr: list[int]) -> None:
    arr_len: int = len(arr)

    for i in range(arr_len):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


def main() -> None:
    arr: list[int] = [2, 5, 4, 1, 3]
    insertion_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()

def selection_sort(arr: list[int]):
    arr_len: int = len(arr)

    for i in range(arr_len):
        min_index: int = i

        for j in range(i + 1, arr_len):
            if arr[j] < arr[j - 1]:
                min_index = j

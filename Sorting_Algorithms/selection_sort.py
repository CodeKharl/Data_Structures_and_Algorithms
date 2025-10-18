from .sort import Sort


class SelectionSort(Sort):
    def sort(self, arr: list[int]) -> None:
        arr_len: int = len(arr)

        for i in range(arr_len):
            min_index: int = i

            for j in range(i + 1, arr_len):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

    def __str__(self) -> str:
        return "Selection Sort"

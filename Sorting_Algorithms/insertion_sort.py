from .sort import Sort


class InsertionSort(Sort):
    def sort(self, arr: list[int]) -> None:
        arr_len: int = len(arr)

        for i in range(arr_len):
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else:
                    break

    def __str__(self) -> str:
        return "Insertion Sort"

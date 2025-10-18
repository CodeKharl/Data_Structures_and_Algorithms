from .sort import Sort


class BubbleSort(Sort):
    def sort(self, arr: list[int]) -> None:
        arr_len: int = len(arr)
        flag: bool = True

        while flag:
            flag = False

            for i in range(1, arr_len):
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    flag = True

    def __str__(self) -> str:
        return "Bubble Sort"

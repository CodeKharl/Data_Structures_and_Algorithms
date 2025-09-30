def search(_list, target):
    start = 0
    end = len(_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if _list[mid] == target:
            return mid
        elif _list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1

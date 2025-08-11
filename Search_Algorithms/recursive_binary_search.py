def search(list, target, start=0, end=None):
    if end is None:
        end = len(list) - 1

    if start > end:
        return -1

    midpoint = (start + end) // 2

    if list[midpoint] == target:
        return midpoint
    elif list[midpoint] > target:
        return search(list, target, start, midpoint - 1)
    else:
        return search(list, target, midpoint + 1, end)


def verify(index_search):
    if index == -1:
        print(f"The target value {target} is not found in the list!")
        return

    print(f"The value {target} found on the list at index = {index}.")


_list = [3, 7, 9]
target = 6
index = search(_list, target)
verify(index)

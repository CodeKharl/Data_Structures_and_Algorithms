def search(_list, target):
    for index in range(0, len(_list)):
        if _list[index] == target:
            return index

    return -1


if __name__ == "__main__":
    _list = [1, 2, 5, 3, 7]
    index = search(_list, 2)

    print("Index :", index)

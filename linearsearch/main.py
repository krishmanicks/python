def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


print(linearSearch([0, 1, 4, 3, 7, 9, 6, 2], 4))
import math


def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            print(list)


def selectionSort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min = j
                list[i], list[min] = list[min], list[i]
    print(list)


def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    print(list)


def bucketsort(list):
    numberofbuckets = round(math.sqrt(len(list)))
    maxvalue = max(list)
    arr = []

    for i in range(numberofbuckets):
        arr.append([])
    for j in list:
        index_b = math.ceil(j*numberofbuckets/maxvalue)
        arr[index_b - 1].append(j)

    for i in range(numberofbuckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(numberofbuckets):
        for j in range(len(arr[i])):
            list[k] = arr[i][j]
            k+=1
    print((list))









cuslist = [2, 1, 7, 6, 5, 3, 4, 9, 8]
insertionSort(cuslist)

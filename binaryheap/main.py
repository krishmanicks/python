class Heap:
    def __init__(self, size):
        self.customlist = (size+1) * [None]
        self.heapsize = 0
        self.maxsize = size + 1

def peek(root):
    if not root:
        return
    else:
        return root.customlist[1]


def sizeofheap(root):
    if not root:
        return
    else:
        print(root.heapsize)


def levelorder(root):
    if not root:
        return
    else:
        for i in range(1, root.heapsize+1):
            print(root.customlist[i])


def heapify(root, index, type):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if type == "min":
        if root.customlist[index] < root.customlist[parentIndex]:
            temp = root.customlist[index]
            root.customlist[index] = root.customlist[parentIndex]
            root.customlist[parentIndex] = temp
        heapify(root, parentIndex, type)
    elif type == "max":
        if root.customlist[index] > root.customlist[parentIndex]:
            temp = root.customlist[index]
            root.customlist[index] = root.customlist[parentIndex]
            root.customlist[parentIndex] = temp
        heapify(root, parentIndex, type)


def insert(root, value, type):
    if root.heapsize + 1 == root.maxsize:
        return "the heap is full"
    root.customlist[root.heapsize + 1] = value
    root.heapsize += 1
    heapify(root, root.heapsize, type)


def heapextract(root, index, type):
    leftindex = index * 2
    rightindex = index * 2 + 1
    swapchild = 0

    if root.heapsize < leftindex:
        return
    elif root.heapsize == leftindex:
        if type == "min":
            if root.customlist[index] > root.customlist[leftindex]:
                temp = root.customlist[index]
                root.customlist[index] = root.customlist[leftindex]
                root.customlist[leftindex] = temp
            return
        else:
            if root.customlist[index] > root.customlist[leftindex]:
                temp = root.customlist[index]
                root.customlist[index] = root.customlist[leftindex]
                root.customlist[leftindex] = temp
            return
    else:
        if type == "min":
            if root.customlist[leftindex] < root.customlist[rightindex]:
                swapchild = leftindex
            else:
                swapchild = rightindex
            if root.customlist[index] > root.customlist[swapchild]:
                temp = root.customlist[index]
                root.customlist[index] = root.customlist[swapchild]
                root.customlist[swapchild] = temp
        else:
            if root.customlist[leftindex] > root.customlist[rightindex]:
                swapchild = leftindex
            else:
                swapchild = rightindex
            if root.customlist[index] < root.customlist[swapchild]:
                temp = root.customlist[index]
                root.customlist[index] = root.customlist[swapchild]
                root.customlist[swapchild] = temp
        heapextract(root, swapchild, type)


def extract(root, type):
    if root. heapsize == 0:
        return
    else:
        extract = root.customlist[1]
        root.customlist[1] = root.customlist[root.heapsize]
        root.customlist[root.heapsize] = None
        root.heapsize -= 1
        heapextract(root, 1, type)
        return  extract


def deleteAll(root):
    root.customlist = None

heap = Heap(5)
sizeofheap(heap)
insert(heap, 4, "max")
insert(heap, 5, "max")
insert(heap, 2, "max")
insert(heap, 1, "max")
insert(heap, 3, "max")
extract(heap, "max")
levelorder(heap)
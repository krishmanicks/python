class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class Doubly:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

# creation
    def create(self, nodevalue):
        node = Node(nodevalue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "created successfully"

    def insert(self, value, location):
        if self.head is None:
            print("the node cannot be inserted")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    def traversal(self):
        if self.head is None:
            print("no elements to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    def reversetraverse(self):
        if self.head is None:
            print("no elements to traverse")
        else:
            print("----------")
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    def search(self, value):
        if self.head is None:
            return "empty list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
            return "value not found"

    def delete(self, location):
        if self.head is None:
            print("no values exists")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            print("successfully deleted")

    def deleteAll(self):
        if self.head is None:
            print("already empty")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
        print("deleted entire list successfully")



doublyL = Doubly()
doublyL.create(34)
print([node.value for node in doublyL])
doublyL.insert(0,0)
doublyL.insert(2,1)
doublyL.insert(5,0)
print([node.value for node in doublyL])
doublyL.traversal()
doublyL.reversetraverse()
print(doublyL.search(34))
doublyL.delete(2)
print([node.value for node in doublyL])
doublyL.deleteAll()


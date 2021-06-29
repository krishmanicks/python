class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoubly:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def create(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode

    def insert(self, value, location):
        if self.head is None:
            print("does not exist")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
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
    print("node has been successfully created")

    def search(self, value):
        if self.head is None:
            return "error"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return "value found"
                if tempNode == self.tail:
                    return "the value does not exist"
                tempNode = tempNode.next

    def delete(self, location):
        if self.head is None:
            print("no elements to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                   self.head.prev = None
                   self.head.next = None
                   self.head = None
                   self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                   self.head.prev = None
                   self.head.next = None
                   self.head = None
                   self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index += 1
                currNode.next = currNode.next.next
                currNode.next.prev = currNode
            print("the node has been successfully deleted")

    def deleteAll(self):
        if self.head is None:
            print("already deleted")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None



circulardoubly = CircularDoubly()
circulardoubly.create(5)
print([node.value for node in circulardoubly])
circulardoubly.insert(1,0)
circulardoubly.insert(2,0)
circulardoubly.insert(3,1)
circulardoubly.insert(4,2)
circulardoubly.insert(6,1)
print([node.value for node in circulardoubly])
print(circulardoubly.search(12))
circulardoubly.delete(3)
print([node.value for node in circulardoubly])
circulardoubly.deleteAll()
print([node.value for node in circulardoubly])
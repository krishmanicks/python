class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Circular:

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

    def create(self, nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = Node
        return "CSLL has been created"

    def insertCLL(self, value, location):
        if self.head is None:
            return "empty"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "created successfully"

    def traversal(self):
        if self.head is None:
            print("empty list")
        else:

            tenode = self.head
            while tenode.next != self.head:
                print(tenode.value)
                tenode = tenode.next

    def search(self, value):
        if self.head is None:
            return " list is empty"
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return " value found"
                node = node.next
                if node == self.tail.next:
                    return "not found"

    def delete(self, location):
        if self.head is None:
            print("no node exists")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail = self.tail
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                nextNode = tempNode.next
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = nextNode.next

    def deleteAll(self):
        self.head = None
        self.tail.next = None
        self.tail = None


circularSLL = Circular()
print(circularSLL.create(12))
circularSLL.insertCLL(0,0)
circularSLL.insertCLL(2,1)
circularSLL.insertCLL(3,1)
circularSLL.insertCLL(4,2)
circularSLL.insertCLL(5,1)
#print(circularSLL.search(12))
circularSLL.traversal()
# print([node.value for node in circularSLL])

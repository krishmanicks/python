class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0:
                newnode.next = self.head
                self.head = newnode
            elif location == 1:
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode

            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode

    def traversalSLL(self):
        if self.head is None:
            print("Linked List empty")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def searchSLL(self, nodevalue):
        if self.head is None:
            return "empty list"
        else:
            node = self.head
            while node is not None:
                if node.value == nodevalue:
                    return "value found"
                node = node.next
            return " the value does not exist"

    def deleteSLL(self, location):
        if self.head is None:
            print("SLL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # Delete entire SLL
    def deleteEntire(self):
        if self.head is None:
            print("the List does not exist")
        else:
            self.head = None
            self.tail = None


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(5, 2)
singlyLinkedList.insertSLL(00, 0)
singlyLinkedList.traversalSLL()
print([node.value for node in singlyLinkedList])
print(singlyLinkedList.searchSLL(33))
singlyLinkedList.deleteEntire()
#singlyLinkedList.deleteSLL()
print([node.value for node in singlyLinkedList])

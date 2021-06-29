class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class doubly:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beg(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
            node.next = None
        else:
            node.next = self.head
            self.head = node

    def insert_end(self, value):
        node = Node(value)
        node.next = None
        self.tail.next = node
        self.tail = node

    def prin(self):
        if self.head is None:
            print("empty linked list")
            return
        var = self.head
        while var:
            print(var.value,end="->")
            var = var.next
        print("None")

    def delete(self):
        if self.head is None:
            print("no value exists")
        else:
            node = self.head
            while node:
                if node.next == self.tail:
                    break
                node = node.next
            node.next = None
            self.tail = node


d = doubly()
d.insert_beg(2)
d.insert_beg(1)
d.insert_beg(0)
d.insert_end(3)
d.insert_end(4)
d.insert_end(5)
d.delete()
d.prin()

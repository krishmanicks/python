class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class doubly:
    def __init__(self):
        self.head = None
        self.tail = None

    def queue(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:

            node.next = self.head
            self.head = node

    def dequeue(self):
        node = self.head
        while node:
            if node.next == self.tail:
                break
            node = node.next
        node.next = None
        self.tail = node

    def display(self):
        var = self.head
        while var:
            print(var.value)
            var = var.next


q = doubly()
q.queue(1)
q.queue(2)
q.queue(3)
q.queue(4)
q.dequeue()
q.display()

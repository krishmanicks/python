class Node:
    def __init__(self, value):
        self.value = None
        self.next = None


class singlylist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = Node
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                    nextnode = tempnode.next
                    tempnode.next = newNode
                    newNode.next = nextnode

    def display(self):
        var = self.head
        while var:
            print(var.value)
            var = var.next


linkly = singlylist()
linkly.insert(1, 0)
linkly.insert(3, 1)
linkly.insert(4, 2)
linkly.display()

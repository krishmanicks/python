class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = next

class Linkedstack:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

class Stack:
    def __init__(self):
        self.Linkedstack = Linkedstack()

    def __str__(self):
        values = [str(x.value) for x in self.Linkedstack]
        return "\n".join(values)

    def isEmpty(self):
        if self.Linkedstack.head is None:
            return  True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.Linkedstack.head
        self.Linkedstack.head = node

    def pop(self):
        if self.isEmpty():
            print("no element to delete")
        else:
            node = self.Linkedstack.head.value
            self.Linkedstack.head = self.Linkedstack.head.next
            print(node)

    def peek(self):
        if self.isEmpty():
            print("no element to peek")
        else:
            node = self.Linkedstack.head.value
            print("peek",node)

    def delete(self):
        self.Linkedstack.head = None


customstack = Stack()
print(customstack.isEmpty())
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)
print(customstack)
print("------")
customstack.pop()
print("------")
print(customstack)
print("--")
customstack.peek()
print("------")
print(customstack)
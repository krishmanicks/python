class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items is None:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.isEmpty():
            print("empty queue")
        else:
            print(self.items.pop(0))

    def peek(self):
        if self.isEmpty():
            print("empty queue")
        else:
            print(self.items[0])

    def delete(self):
        self.items = None


customQ = Queue()
print(customQ.isEmpty())
customQ.enqueue(1)
customQ.enqueue(2)
customQ.enqueue(3)
customQ.enqueue(4)
print(customQ)
customQ.dequeue()
print(customQ)
customQ.peek()
print(customQ)



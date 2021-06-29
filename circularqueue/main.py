class Queue:

    def __init__(self, maxsize):
        self.items = maxsize * [None]
        self.maxsize = maxsize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxsize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            return "the Q is full"
        else:
            if self.top + 1 == self.maxsize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value

    def dequeue(self):
        if self.isEmpty():
            return "empty Q"
        else:
            firstelement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxsize:
                self.start = 0
            else:
                self.start += 1
            self.items [start] = None
            return firstelement

    def peek(self):
        if self.isEmpty():
            return "empty Q"
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.maxsize * [None]
        self.top = -1
        self.start = -1

customQ = Queue(4)
print(customQ.isFull())
print(customQ.isEmpty())
customQ.enqueue(1)
customQ.enqueue(2)
customQ.enqueue(3)
customQ.enqueue(4)
print(customQ)
customQ.dequeue()
print("---")
print(customQ)
print(customQ.peek())


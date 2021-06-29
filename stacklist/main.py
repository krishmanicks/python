class Stack:
    def __init__(self):
        self.list = []

    #def __str__(self):
     #   value = self.list.reverse()
      #  value = [str(x) for x in self.list]
       # return '\n'.join(value)

    def disp(self):
        for info in reversed(self.list):
            print(info)


    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return "pushed successfully"

    def pop(self):
        if self.isEmpty():
            return "there is no element in the stack"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "empty stack"
        else:
            return self.list[(len(self.list)-1)]

    def delete(self):
        self.list = None
        print("stack is empty")


customstack = Stack()
customstack.isEmpty()
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)
customstack.disp()
print("--1--")
print(customstack.pop())
print("----23--")
customstack.disp()
print("--  3--")
print(customstack.peek())
customstack.disp()
print("--4--")
customstack.delete()
customstack.disp()
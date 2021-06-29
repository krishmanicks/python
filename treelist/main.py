# create
class BinaryTree:
    def __init__(self, size):
        self.customlist = size * [None]
        self.lastusedindex = 0
        self.maxsize = size

    def insertnode(self, value):
        if self.lastusedindex + 1 == self.maxsize:
            return "empty tree"
        self.customlist[self.lastusedindex+1] = value
        self.lastusedindex += 1

    def searchnode(self, nodevalue):
        for i in range(len(self.customlist)):
            if self.customlist[i] == nodevalue:
                return "success"
        return "not found"

    def preorder(self,index):
        if index > self.lastusedindex:
            return
        print(self.customlist[index])
        self.preorder(index*2)
        self.preorder(index*2 + 1)

    def inorder(self,index):
        if index > self.lastusedindex:
            return
        self.inorder(index*2)
        print(self.customlist[index])
        self.inorder(index*2 + 1)

    def postorder(self,index):
        if index > self.lastusedindex:
            return
        self.postorder(index*2)
        self.postorder(index*2 + 1)
        print(self.customlist[index])

    def levelorder(self, index):
        for i in range(index, self.lastusedindex+1):
            print(self.customlist[i])

    def delete(self, value):
        if self.lastusedindex == 0:
            return "nothing to delete"
        for i in range(1, self.lastusedindex+1):
            if self.customlist[i] == value:
                self.customlist[i] = self.customlist[self.lastusedindex]
                self.customlist[self.lastusedindex] = None
                self.lastusedindex -= 1
                return "success"

    def deleteAll(self):
        self.customlist = None
        print("done")



newBt = BinaryTree(8)
(newBt.insertnode("drinks"))
(newBt.insertnode("hot"))
(newBt.insertnode("cold"))
(newBt.insertnode("tea"))
(newBt.insertnode("coffee"))
print(newBt.searchnode("cold"))
newBt.preorder(1)
print("------inorder--------")
newBt.inorder(1)
print("----post----------")
newBt.postorder(1)
print("--level------")
print(newBt.delete("coffee"))
newBt.levelorder(1)
newBt.deleteAll()


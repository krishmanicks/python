class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


def insertNode(rootnode, nodevalue):
    if rootnode.data is None:
        rootnode.data = nodevalue
    elif nodevalue <= rootnode.data:
        if rootnode.leftchild is None:
            rootnode.leftchild = BSTNode(nodevalue)
        else:
            insertNode(rootnode.leftchild, nodevalue)
    else:
        if rootnode.rightchild is None:
            rootnode.rightchild = BSTNode(nodevalue)
        else:
            insertNode(rootnode.rightchild, nodevalue)


def preorder(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preorder(rootnode.leftchild)
    preorder(rootnode.rightchild)


def inorder(rootnode):
    if not rootnode:
        return
    inorder(rootnode.leftchild)
    print(rootnode.data)
    inorder(rootnode.rightchild)


def postorder(rootnode):
    if not rootnode:
        return
    postorder(rootnode.leftchild)
    postorder(rootnode.rightchild)
    print(rootnode.data)


def search(rootnode, value):
    if rootnode.data == value:
        print("value found")
    elif value < rootnode.data:
        if rootnode.leftchild.data == value:
            print("the value is found")
        else:
            search(rootnode.leftchild, value)
    else:
        if rootnode.rightchild.data == value:
            print("the value is found")
        else:
            search(rootnode.rightchild, value)


def minvalue(bstnode):
    current = bstnode
    while current.leftchild is not None:
        current = current.leftchild
    return current


def delete(rootnode, value):
    if rootnode is None:
        return rootnode
    if value < rootnode.data:
        rootnode.leftchild = delete(rootnode.leftchild, value)
    elif value > rootnode.data:
        rootnode.rightchild = delete(rootnode.rightchild, value)
    else:
        if rootnode.leftchild is None:
            temp = rootnode.rightchild
            rootnode = None
            return temp
        if rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp

        temp = minvalue(rootnode.rightchild)
        rootnode.data = temp.data
        rootnode.rightchild = delete(rootnode.rightchild, temp.data)
        return rootnode

def deleteAll(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None


def printLevelOrder(root):
    if root is None:
        return
    q = []
    q.append(root)

    while q:
        count = len(q)
        while count > 0:
            temp = q.pop(0)
            print(temp.data, end=' ')
            if temp.leftchild:
                q.append(temp.leftchild)
            if temp.rightchild:
                q.append(temp.rightchild)

            count -= 1
        print(' ')


newbst = BSTNode(None)
insertNode(newbst, 70)
insertNode(newbst, 50)
insertNode(newbst, 90)
insertNode(newbst, 30)
insertNode(newbst, 60)
insertNode(newbst, 80)
insertNode(newbst, 100)
insertNode(newbst, 20)
insertNode(newbst, 40)
preorder(newbst)
print("----inorder----")
inorder(newbst)
print("----post----")
postorder(newbst)
search(newbst, 70)
#delete(newbst, 100)
printLevelOrder(newbst)

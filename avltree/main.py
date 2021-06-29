class AvlNode:
    def __init__(self, data):
        self.data = data
        self.rightchild = None
        self.leftchild = None
        self.height = 1


def preorder(root):
    if root is None:
        return
    print(root.data)
    preorder(root.leftchild)
    preorder(root.rightchild)


def inorder(root):
    if not root:
        return
    inorder(root.leftchild)
    print(root.data)
    inorder(root.rightchild)


def postorder(root):
    if not root:
        return
    postorder(root.leftchild)
    postorder(root.rightchild)
    print(root.data)


def LevelOrder(root):
    if root is None:
        return
    q = [root]
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


def search(root, value):
    if root.data == value:
        print("value found")
    elif value < root.data:
        if root.leftchild.data == value:
            print("the value is found")
        else:
            search(root.leftchild, value)
    else:
        if root.rightchild.data == value:
            print("the value is found")
        else:
            search(root.rightchild, value)


def getheight(root):
    if not root:
        return 0
    return root.height


def rightrotate(disbalanenode):
    newroot = disbalanenode.leftchild
    disbalanenode.leftchild = disbalanenode.leftchild.rightchild
    newroot.rightchild = disbalanenode
    disbalanenode.height = 1 + max(getheight(disbalanenode.leftchild), getheight(disbalanenode.rightchild))
    newroot.height = 1 + max(getheight(newroot.leftchild), getheight(newroot.rightchild))
    return newroot


def leftrotate(disbalancenode):
    newroot = disbalancenode.rightchild
    disbalancenode.rightchild = disbalancenode.rightchild.leftchild
    newroot.leftchild = disbalancenode
    disbalancenode.height = 1 + max(getheight(disbalancenode.leftchild), getheight(disbalancenode.rightchild))
    newroot.height = 1 + max(getheight(newroot.leftchild), getheight(newroot.rightchild))
    return newroot


def getbalance(root):
    if not root:
        return 0
    return getheight(root.leftchild) - getheight(root.rightchild)


def insert(root, value):
    if not root:
        return AvlNode(value)
    elif value < root.data:
        root.leftchild = insert(root.leftchild, value)
    else:
        root.rightchild = insert(root.rightchild, value)

    root.height = 1 + max(getheight(root.leftchild), getheight(root.rightchild))
    balance = getbalance(root)
    if balance > 1 and value < root.leftchild.data:
        return rightrotate(root)
    if balance > 1 and value > root.leftchild.data:
        root.leftchild = leftrotate(root.leftchild)
        return rightrotate(root)
    if balance < -1 and value > root.rightchild.data:
        return leftrotate(root)
    if balance < -1 and value < root.rightchild.data:
        root.rightchild = rightrotate(root.rightchild)
        return leftrotate(root)
    return root


def getmin(root):
    if root is None or root.leftchild is None:
        return root
    return getmin(root.leftchild)


def delete(root, value):
    if root is None:
        return root
    elif value < root.data:
        root.leftchild = delete(root.leftchild, value)
    elif value > root.data:
        root.rightchild = delete(root.rightchild, value)
    else:
        if root.leftchild is None:
            temp = root.rightchild
            root.data = None
            return temp
        elif root.rightchild is None:
            temp = root.leftchild
            root.data = None
            return temp
        temp = getmin(root.rightchild)
        root.data = temp.data
        root.rightchild = delete(root.rightchild, temp.data)
    balance = getbalance(root)
    if balance > 1 and getbalance(root.leftchild) >= 0:
        return rightrotate(root)
    if balance < -1 and getbalance(root.rightchild) <= 0:
        return leftrotate(root)
    if balance > 1 and getbalance(root.leftchild) < 0:
        root.leftchild = leftrotate(root.leftchild)
        return rightrotate(root)
    if balance < -1 and getbalance(root.rightchild) > 0:
        root.rightchild = rightrotate(root.rightchild)
        return leftrotate(root)
    return root


def deleteAll(root):
    root.data = None
    root.leftchild = None
    root.rightchild = None
    print("successfully deleted")


newavl = AvlNode(5)
newavl = insert(newavl, 10)
newavl = insert(newavl, 15)
newavl = insert(newavl, 20)
newavl = delete(newavl, 15)
LevelOrder(newavl)
search(newavl, 10)

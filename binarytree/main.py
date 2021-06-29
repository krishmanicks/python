class TreeNode:
    def __init__(self, data):
        self.data = data
        self.rightchild = None
        self.leftchild = None


newBT = TreeNode("drinks")
leftchild = TreeNode("hot")
tea = TreeNode("Tea")
coffee = TreeNode("coffee")
leftchild.leftchild = tea
leftchild.rightchild = coffee
rightchild = TreeNode("cold")
newBT.leftchild = leftchild
newBT.rightchild = rightchild

def preorderTraversal(rootnode):
    if not rootnode:
        return                                                      #root node -> left -> right
    print(rootnode.data)
    preorderTraversal(rootnode.leftchild)
    preorderTraversal(rootnode.rightchild)

preorderTraversal(newBT)

print("----------------")

def inorderTraversal(rootnode):
    if not rootnode:
        return                                                      #left -> root -> right
    inorderTraversal(rootnode.leftchild)
    print(rootnode.data)
    inorderTraversal(rootnode.rightchild)

inorderTraversal(newBT)

print("--------------------")

def postorderTraversal(rootnode):
    if not rootnode:
        return                                                        #left - > right -> root
    postorderTraversal(rootnode.leftchild)
    postorderTraversal(rootnode.rightchild)
    print(rootnode.data)

postorderTraversal(newBT)

#search
def inorder(rootnode, key):
    if (rootnode == None):
        return False

    if (rootnode.data == key):
        return True
    res1 = inorder(rootnode.leftchild, key)
    if res1:
        return True
    res2 = inorder(rootnode.rightchild, key)
    return res2

print("----")
key = "colds"
if (inorder(newBT, key)):
    print("YES")
else:
    print("NO")

print("---"
      "----"
      "-----------------")

def deleteAll(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None
    print("successfully deleted")

deleteAll(newBT)
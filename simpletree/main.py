class Treenode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        value = " " * level + str(self.data) + "\n"
        for child in self.children:
            value += child.__str__(level + 1)
        return value

    def addchild(self, Treenode):
        self.children.append(Treenode)

tree = Treenode("drinks", [])
cold = Treenode("cold", [])
hot = Treenode("hot", [])
cola = Treenode("cola", [])
cola = Treenode("cola", [])
fanta = Treenode("fanta", [])
tea = Treenode("tea", [])
coffee = Treenode("coffee", [])
tree.addchild(cold)
tree.addchild(hot)
cold.addchild(cola)
cold.addchild(fanta)
hot.addchild(tea)
hot.addchild(coffee)
print(tree)
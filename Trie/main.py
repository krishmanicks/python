class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofstring = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node is None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endofstring = True
        print("success")

    def searchstring(self, word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node is None:
                return False
            current = node

        if current.endofstring is True:
            return True
        else:
            return False


def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canthisnodebedeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False

    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endofstring = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentNode.endofstring is True:
        deleteString(currentNode, word, index+1)
        return False

    canthisnodebedeleted = deleteString(currentNode, word, index+1)
    if canthisnodebedeleted is True:
        root.children.pop(ch)
        return True
    else:
        return False


newTrie = Trie()
newTrie.insert("App")
newTrie.insert("Appl")
deleteString(newTrie.root, "App", 0)
print(newTrie.searchstring("App"))


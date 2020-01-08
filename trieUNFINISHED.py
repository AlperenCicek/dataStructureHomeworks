class TrieNode:
    def __init__(self, data, isThatWord):
        self.data = data
        self.isThatWord = isThatWord
        self.children = []

class Trie:
    def __init__(self):
        self.head = None

    def add(self, data):
        word = data
        head = self.head
        counter = 0
        for letter in word:
            newNode = TrieNode(str(letter), False)
            head.children.append(newNode)
            head = head.children[counter]
            counter += 1

    def printFunc(self):
        head = self.head
        while head is not None:
            print(head.data)
            head = head.children[0]






root = TrieNode("", False)
trie = Trie()
trie.head = root
trie.add("asdfg")
trie.printFunc()
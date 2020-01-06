class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


    def addingNewNode(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.addingNewNode(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.addingNewNode(data)
        else:
            self.data = data

    def remove(self):
        self.data = None

    def printFunc(self):
        if self.left:
            self.left.printFunc()
        print( self.data)
        if self.right:
            self.right.printFunc()
        
    def UI(self):
        while 1:
            print("How many nodes do you want to enter?")
            numberOfNodes = int(input())
            for i in range(1, numberOfNodes + 1):
                print(i,". element:")
                inputValue = int(input())
                Nodes.addingNewNode(inputValue)
            print("Here ordered numbers:")
            Nodes.printFunc()


Nodes = Node(10)
Nodes.remove()
Nodes.UI()
class Node:
    def __init__(self, data):
        self.data = data
        self.head = None
        self.next = None
        self.prev = None

    class NodeA:
        def __init__(self, data):
            Node.__init__(self, data)
    
    class NodeB:
        def __init__(self, data):
            Node.__init__(self, data)

class LinkedList:  
    def __init__(self):
        self.head = None

    def addingNewNodeToEnd(self, data):
        head = self.head
        if data == "a":
            newNode = Node.NodeA(data)
        elif data == "b":
            newNode = Node.NodeB(data)
        while head.next is not None:
            head = head.next
        
        newNode.prev = head
        head.next = newNode

    def addingNewNodeAsFirst(self, data):
        if data == "a":
            newNode = Node.NodeA(data)
        elif data == "b":
            newNode = Node.NodeB(data)
        self.head = newNode
    
    def listing(self):
        head = self.head
        print("These are our list:")
        while head is not None:
            print(head.data)
            head = head.next
    
    def removeNodeFromBeginnig(self):
        head = self.head
        head.data = None
        head.next.prev = None
        self.head = head.next

    def removeNodeFromEnd(self):
        head = self.head
        while head.next.next != None:
            head = head.next

        
        head.next.prev = None
        head.next = None
        
    def checkForRegular(self):
        head = self.head
        counterA = 0
        counterB = 0
        while head is not None:
            if head.data == "a":
                counterA += 1
            elif head.data == "b":
                counterB += 1
            
            head = head.next
        print(counterA, "piece(s) a,", counterB, "piece(s) b")
        check = False
        while check == False:
            counterB *= 2
            if counterB == counterA:
                check = True
            else:
                break

        if check:
            print("IT'S REGULAR!")
        else:
            print("IT'S NOT REGULAR!")
    

class Word:
    def __init__(self, data):
        self.data = data

    def splitTheWord(self):
        data = self.data
        counter = 0
        for x in range(0, len(data)):
            if counter == 0:
                LinkedList.addingNewNodeAsFirst(self, data[x])
            else:
                LinkedList.addingNewNodeToEnd(self, data[x])
            counter += 1
        LinkedList.listing(self)
        LinkedList.checkForRegular(self)
    
while 1:
    print("Enter the string to check it is regular or not!:(Format must be like that 'aaabb')")
    inputValue = str(input())
    word = Word(inputValue)
    word.splitTheWord()
    


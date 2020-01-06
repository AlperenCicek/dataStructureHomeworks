class Node:
    def __init__(self, data = None):
        self.data = data
        self.head = None
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listing(self):
        head = self.head
        print("These are our list:")
        while head is not None:
            print(head.data)
            head = head.next

    def addingNewNodeToEnd(self, data):
        head = self.head
        newNode = Node(data)
        while head.next is not None:
            head = head.next
        
        newNode.prev = head
        head.next = newNode
        
    
    def addingNewNodeAsFirst(self, data):
        newNode = Node(data)
        self.head = newNode

    def addingFunc(self, data):
        if self.head is not None:
            LinkedList.addingNewNodeToEnd(self, data)
        else:
            LinkedList.addingNewNodeAsFirst(self, data)


    def removeNodeWithData(self, data):
        head = self.head
        while head.next != None:
            
            if head.data == data:
                head.data = None
                self.head = head.next

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

    def removeNodeIfThereIsOne(self):
        head = self.head
        head.data = None
        self.head = None
        print("It's palindrome!")

    def remove(self):
        head = self.head

        if head == None:
            print("There is no Node to delete!")
        elif head.data != None and head.next == None:
            LinkedList.removeNodeIfThereIsOne(self)
        else:  
            firstValue = self.head
            while head.next is not None:
                head = head.next
            lastValue = head  
            if firstValue.data == lastValue.data:
                LinkedList.removeNodeFromBeginnig(self)
                LinkedList.removeNodeFromEnd(self)
            else:
                print("It's not palindrome!")

    def gettingValues(self):
        check = False
        while check != True:
            print("How many element do you input?:(Please enter odd numbers beacuse of palindrome rules)")
            numberOfElement = int(input())
            if numberOfElement%2 == 1:
                for i in range(1, numberOfElement + 1):

                    print("Enter the", i, "element:")
                    value = input()
                    LinkedList.addingFunc(self, value)
                    check = True
            else:
                print("It's not palindrome because of number of element.")
    def UI(self):

        LinkedList.gettingValues(self)
        while 1:
            print("\nWhich operation do you want to select?:(0:New / 1:Listing / 2:Deleting / 3:Exit)")
            numberOfOperator = int(input())
            if numberOfOperator == 0:
                LinkedList.gettingValues(self)
            elif numberOfOperator == 1:
                words.listing()
            elif numberOfOperator == 2:
                words.remove()
            elif numberOfOperator == 3:
                break
            else:
                print("Wrong input!")

words = LinkedList()
words.UI()           
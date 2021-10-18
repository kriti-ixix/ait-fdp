class LinkedList:
    def __init__(self):
        self.head = None 

    def printList(self):
        temp = self.head
        
        while temp:
            print(temp.data)
            temp = temp.next

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


linkedList = LinkedList()
linkedList.head = Node(1)
second = Node(20)
third = Node(25)

linkedList.head.next = second
second.next = third

linkedList.printList()
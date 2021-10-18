class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    def printList(self):
        temp = self.data

        while temp:
            print(f"Node: {temp}")
            print(f"Left node: {self.left}")
            print(f"Right node: {self.right}")

            temp = self.left

    def __str__(self):
        return str(self.data)


root = Node(10)
root.left = Node(5)
root.right = Node(12)
root.left.left = Node(3)

root.printList()
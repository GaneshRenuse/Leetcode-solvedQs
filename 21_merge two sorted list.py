class Node:
    def __init__(self, head):
        self.head = head
        self.next = None

    def newnode(self, head):
        return Node(head)


a = Node(0)
a.next = Node(7)
a.next.next = Node(5)

while a.head is not None:
    print(a.head, end=" ")
    a.head = a.next

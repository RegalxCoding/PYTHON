class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def display(self):
        current = self.head
        if self.head is None:
            print("Linked List is empty")
            return
        print("Nodes of linked list are:")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def addToLast(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

    def addToFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        if self.tail is None:
            self.tail = newNode

    def delAtFirst(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
        else:
            self.head = self.head.next
            if self.head is None:
                self.tail = None

    def delAtLast(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
            self.tail = current

# User interaction
slist = SinglyLinkedList()
while True:
    print("\nOptions:\n1. Add Node at End\n2. Add Node at Start\n3. Delete First Node\n4. Delete Last Node\n5. Display\n6. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        data = int(input("Enter data to add at the end: "))
        slist.addToLast(data)
    elif choice == 2:
        data = int(input("Enter data to add at the start: "))
        slist.addToFirst(data)
    elif choice == 3:
        slist.delAtFirst()
    elif choice == 4:
        slist.delAtLast()
    elif choice == 5:
        slist.display()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.head is None:  # If the list is empty
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:  # If the list is empty
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def insertAtPosition(self, data, pos):
        if pos == 1:
            self.insertAtBeginning(data)
        else:
            newNode = Node(data)
            current = self.head
            count = 1
            while current is not None and count < pos - 1:
                current = current.next
                count += 1
            if current is None:
                print("Position out of bounds!")
            else:
                newNode.next = current.next
                newNode.prev = current
                if current.next:
                    current.next.prev = newNode
                current.next = newNode
                if newNode.next is None:
                    self.tail = newNode

    def deleteAtBeginning(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
        else:
            if self.head.next is None:  # Single node case
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def deleteAtEnd(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
        elif self.head.next is None:  # Single node case
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def deleteAtPosition(self, pos):
        if pos == 1:
            self.deleteAtBeginning()
        else:
            current = self.head
            count = 1
            while current is not None and count < pos:
                current = current.next
                count += 1
            if current is None:
                print("Position out of bounds!")
            else:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                if current == self.tail:
                    self.tail = current.prev

    def traverse(self):
        if self.head is None:
            print("List is empty.")
        else:
            print("Nodes in the linked list are:")
            current = self.head
            while current:
                print(current.data, end=" <-> ")
                current = current.next
            print("None")

# Menu-driven program
dll = DoublyLinkedList()
while True:
    print("\nMenu:")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Specific Position")
    print("4. Delete at Beginning")
    print("5. Delete at End")
    print("6. Delete at Specific Position")
    print("7. Traverse the List")
    print("8. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data to insert at the beginning: "))
        dll.insertAtBeginning(data)
    elif choice == 2:
        data = int(input("Enter data to insert at the end: "))
        dll.insertAtEnd(data)
    elif choice == 3:
        data = int(input("Enter data to insert: "))
        pos = int(input("Enter position to insert: "))
        dll.insertAtPosition(data, pos)
    elif choice == 4:
        dll.deleteAtBeginning()
    elif choice == 5:
        dll.deleteAtEnd()
    elif choice == 6:
        pos = int(input("Enter position to delete: "))
        dll.deleteAtPosition(pos)
    elif choice == 7:
        dll.traverse()
    elif choice == 8:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

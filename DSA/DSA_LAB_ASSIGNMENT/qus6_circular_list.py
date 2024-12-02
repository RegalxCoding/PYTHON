class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.head is None:  # Empty list case
            self.head = newNode
            newNode.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newNode.next = self.head
            temp.next = newNode
            self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:  # Empty list case
            self.head = newNode
            newNode.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head

    def insertAtPosition(self, data, pos):
        if pos == 1:
            self.insertAtBeginning(data)
        else:
            newNode = Node(data)
            temp = self.head
            count = 1
            while count < pos - 1 and temp.next != self.head:
                temp = temp.next
                count += 1
            if count < pos - 1:
                print("Position out of bounds!")
            else:
                newNode.next = temp.next
                temp.next = newNode

    def deleteAtBeginning(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
        elif self.head.next == self.head:  # Single node case
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
        elif self.head.next == self.head:  # Single node case
            self.head = None
        else:
            temp = self.head
            prev = None
            while temp.next != self.head:
                prev = temp
                temp = temp.next
            prev.next = self.head

    def deleteAtPosition(self, pos):
        if self.head is None:
            print("List is empty, nothing to delete.")
        elif pos == 1:
            self.deleteAtBeginning()
        else:
            temp = self.head
            count = 1
            prev = None
            while count < pos and temp.next != self.head:
                prev = temp
                temp = temp.next
                count += 1
            if count < pos:
                print("Position out of bounds!")
            else:
                prev.next = temp.next

    def traverse(self):
        if self.head is None:
            print("List is empty.")
        else:
            temp = self.head
            print("Nodes in the circular linked list are:")
            while True:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == self.head:
                    break
            print("(Back to Head)")

# Menu-driven program
cll = CircularLinkedList()
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
        cll.insertAtBeginning(data)
    elif choice == 2:
        data = int(input("Enter data to insert at the end: "))
        cll.insertAtEnd(data)
    elif choice == 3:
        data = int(input("Enter data to insert: "))
        pos = int(input("Enter position to insert: "))
        cll.insertAtPosition(data, pos)
    elif choice == 4:
        cll.deleteAtBeginning()
    elif choice == 5:
        cll.deleteAtEnd()
    elif choice == 6:
        pos = int(input("Enter position to delete: "))
        cll.deleteAtPosition(pos)
    elif choice == 7:
        cll.traverse()
    elif choice == 8:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

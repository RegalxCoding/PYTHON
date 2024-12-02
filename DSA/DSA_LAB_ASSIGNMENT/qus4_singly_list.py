class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNodeAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def addNodeAtStart(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        if self.tail is None:
            self.tail = newNode

    def addNodeAtPosition(self, data, pos):
        newNode = Node(data)
        if pos == 1:  # At the beginning
            self.addNodeAtStart(data)
        else:
            current = self.head
            count = 1
            while current is not None and count < pos - 1:
                current = current.next
                count += 1
            if current is None:
                print("Position out of bounds!")
            else:
                newNode.next = current.next
                current.next = newNode
                if newNode.next is None:
                    self.tail = newNode

    def deleteAtStart(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
        else:
            self.head = self.head.next
            if self.head is None:
                self.tail = None

    def deleteAtEnd(self):
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

    def deleteAtPosition(self, pos):
        if pos == 1:  # At the beginning
            self.deleteAtStart()
        else:
            current = self.head
            count = 1
            while current is not None and count < pos - 1:
                current = current.next
                count += 1
            if current is None or current.next is None:
                print("Position out of bounds!")
            else:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current

    def traverse(self):
        current = self.head
        if current is None:
            print("List is empty.")
        else:
            print("Nodes in the linked list are:")
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("List reversed successfully.")

# Menu-driven program
slist = SinglyLinkedList()
while True:
    print("\nMenu:")
    print("1. Insert at Start")
    print("2. Insert at End")
    print("3. Insert at Specific Position")
    print("4. Delete at Start")
    print("5. Delete at End")
    print("6. Delete at Specific Position")
    print("7. Traverse the List")
    print("8. Reverse the List")
    print("9. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data to insert at the start: "))
        slist.addNodeAtStart(data)
    elif choice == 2:
        data = int(input("Enter data to insert at the end: "))
        slist.addNodeAtEnd(data)
    elif choice == 3:
        data = int(input("Enter data to insert: "))
        pos = int(input("Enter position to insert: "))
        slist.addNodeAtPosition(data, pos)
    elif choice == 4:
        slist.deleteAtStart()
    elif choice == 5:
        slist.deleteAtEnd()
    elif choice == 6:
        pos = int(input("Enter position to delete: "))
        slist.deleteAtPosition(pos)
    elif choice == 7:
        slist.traverse()
    elif choice == 8:
        slist.reverse()
    elif choice == 9:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

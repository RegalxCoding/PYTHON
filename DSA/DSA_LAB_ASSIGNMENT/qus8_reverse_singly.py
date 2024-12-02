# Algorithm to Reverse a Singly Linked List
#1. Initialize Pointers:

# Create three pointers: prev (set to None), current (set to the head of the list), and next_node (to hold the next node temporarily).
# 2.Iterate Through the List:

# While current is not None:
# Save the next node: next_node = current.next.
# Reverse the link: Set current.next = prev.
# Move the pointers forward: prev = current and current = next_node.
#3. Update Head:

# After the loop, set the head of the list to prev.
# 4.The list is now reversed.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev forward
            current = next_node       # Move current forward
        self.head = prev  # Update head to the last node

    def display(self):
        if self.head is None:
            print("List is empty.")
        else:
            current = self.head
            print("Nodes in the linked list are:")
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

# Driver Code
sll = SinglyLinkedList()
while True:
    print("\nMenu:")
    print("1. Add Node")
    print("2. Reverse List")
    print("3. Display List")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data to add: "))
        sll.addNode(data)
    elif choice == 2:
        sll.reverse()
        print("List reversed successfully.")
    elif choice == 3:
        sll.display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

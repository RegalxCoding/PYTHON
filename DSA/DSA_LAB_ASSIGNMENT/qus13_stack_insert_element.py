# Algorithm to Insert an Element into a Stack Using Linked List
# 1.Create a Node:

# Define a structure Node with two parts: data (to store the element) and next (to point to the next node).
# 2.Create Stack Class:

# Initialize top to None in the stack class to represent the empty stack.
# 3.Insertion (Push Operation):

# Allocate memory for a new node and assign the data.
# Set the next pointer of the new node to point to the current top.
# Update the top pointer to point to the new node.
# 4. Check for Empty Stack:

# If top is None, the stack is empty.
# 5.Traverse (Display Stack):

# Starting from top, traverse the linked list using the next pointer and display the elements.
# Node class representing each element in the stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class using a linked list
class Stack:
    def __init__(self):
        self.top = None  # Initialize top to None (empty stack)

    # Check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Push operation to insert an element into the stack
    def push(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.top  # Link the new node to the current top
        self.top = new_node  # Update the top pointer
        print(f"{data} pushed onto the stack.")

    # Display the stack
    def traverse(self):
        if self.is_empty():
            print("Stack is empty. Nothing to display.")
        else:
            print("Stack elements (top to bottom):")
            current = self.top
            while current:
                if current == self.top:
                    print(f"{current.data} <=== TOP")
                else:
                    print(current.data)
                current = current.next

# Driver Code
stack = Stack()
while True:
    print("\n!!! STACK INSERTION USING LINKED LIST !!!")
    print("1. PUSH")
    print("2. DISPLAY STACK")
    print("0. EXIT")

    # User's choice
    choice = int(input("Enter your choice: "))

    if choice == 1:  # Push
        value = int(input("Enter value to push: "))
        stack.push(value)

    elif choice == 2:  # Traverse
        stack.traverse()

    elif choice == 0:  # Exit
        print("Exiting... Bye!")
        break

    else:  # Invalid choice
        print("Invalid choice. Please try again.")


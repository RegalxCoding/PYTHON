# Node class representing each element in the stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class using a linked list
class Stack:
    def __init__(self):
        self.top = None  # Top points to the top node in the stack

    # Check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Push operation to add an element at the top
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"{data} pushed onto the stack.")

    # Pop operation to remove and return the top element
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Nothing to pop.")
        else:
            popped_data = self.top.data
            self.top = self.top.next
            print(f"Popped item: {popped_data}")

    # Peek operation to view the top element without removing it
    def peek(self):
        if self.is_empty():
            print("Stack is empty. No top element.")
        else:
            print(f"Top element: {self.top.data}")

    # Traverse operation to display all elements in the stack
    def traverse(self):
        if self.is_empty():
            print("Stack is empty. Nothing to show.")
        else:
            print("Stack elements (top to bottom):")
            current = self.top
            while current:
                if current == self.top:
                    print(f"{current.data} <=== TOP")
                else:
                    print(current.data)
                current = current.next

# Menu-driven program for stack operations
stack = Stack()
while True:
    print("\n!!! STACK OPERATIONS USING LINKED LIST !!!")
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. TRAVERSE")
    print("0. EXIT")

    # User's choice
    choice = int(input("Enter your choice: "))

    if choice == 1:  # Push
        value = int(input("Enter value to push: "))
        stack.push(value)

    elif choice == 2:  # Pop
        stack.pop()

    elif choice == 3:  # Peek
        stack.peek()

    elif choice == 4:  # Traverse
        stack.traverse()

    elif choice == 0:  # Exit
        print("Exiting... Bye!")
        break

    else:  # Invalid choice
        print("Invalid choice. Please try again.")

# Stack Implementation Using Array

# Initialize an empty stack
stack = []

# Function to check if the stack is empty
def is_empty(stack):
    return len(stack) == 0

# Function to push an item onto the stack
def push(stack, item):
    stack.append(item)
    print(f"{item} pushed onto the stack.")

# Function to pop an item from the stack
def pop(stack):
    if is_empty(stack):
        print("Stack is empty. Nothing to pop.")
    else:
        popped_item = stack.pop()  # Removes and returns the last item
        print(f"Popped item: {popped_item}")

# Function to peek at the top item of the stack
def peek(stack):
    if is_empty(stack):
        print("Stack is empty. No top element.")
    else:
        print(f"Top element: {stack[-1]}")

# Function to display all items in the stack
def show(stack):
    if is_empty(stack):
        print("Stack is empty. Nothing to show.")
    else:
        print("Stack elements (top to bottom):")
        for i in range(len(stack) - 1, -1, -1):  # Traverse from top to bottom
            if i == len(stack) - 1:
                print(f"{stack[i]} <=== TOP")
            else:
                print(stack[i])

# Menu-driven program
while True:
    print("\n!!! STACK OPERATIONS !!!")
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. SHOW STACK")
    print("0. EXIT")

    # User's choice
    choice = int(input("Enter your choice: "))

    if choice == 1:  # Push
        value = int(input("Enter value to push: "))
        push(stack, value)

    elif choice == 2:  # Pop
        pop(stack)

    elif choice == 3:  # Peek
        peek(stack)

    elif choice == 4:  # Show stack
        show(stack)

    elif choice == 0:  # Exit
        print("Exiting... Bye!")
        break

    else:  # Invalid choice
        print("Invalid choice. Please try again.")

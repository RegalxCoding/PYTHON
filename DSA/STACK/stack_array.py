class Stack:
    def __init__(self, size):
        self.stack = []  # Array to store stack elements
        self.size = size  # Maximum size of the stack
    
    def push(self, data):
        # Algorithm for Push
        if len(self.stack) == self.size:
            print("Stack Overflow! Cannot push more elements.")
            return
        self.stack.append(data)
        print(f"{data} pushed into the stack.")
    
    def pop(self):
        # Algorithm for Pop
        if self.is_empty():
            print("Stack Underflow! No elements to pop.")
            return
        popped_data = self.stack.pop()
        print(f"{popped_data} popped successfully.")
    
    def peek(self):
        # Algorithm for Peek
        if self.is_empty():
            print("Stack is empty.")
            return
        print(f"Top of Stack: {self.stack[-1]}")
    
    def traverse(self):
        # Algorithm for Traverse
        if self.is_empty():
            print("Stack is empty.")
            return
        print("Stack elements are:")
        for element in reversed(self.stack):  # Reverse for stack order
            print(element)
    
    def is_empty(self):
        # Algorithm for is_empty
        return len(self.stack) == 0

# Example usage:
if __name__ == "__main__":
    stack = Stack(5)  # Stack of size 5
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.traverse()
    stack.peek()
    stack.pop()
    stack.traverse()
    stack.pop()
    stack.pop()
    stack.pop()  # Attempt to pop from empty stack

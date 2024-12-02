# Node class representing each element in the queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class using a linked list
class Queue:
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue

    # Check if the queue is empty
    def is_empty(self):
        return self.front is None

    # Enqueue operation to insert an element into the queue
    def enqueue(self, data):
        new_node = Node(data)  # Create a new node
        if self.is_empty():
            self.front = self.rear = new_node  # First node is both front and rear
        else:
            self.rear.next = new_node  # Link the new node to the rear
            self.rear = new_node  # Update the rear to the new node
        print(f"{data} inserted into the queue.")

    # Dequeue operation to remove an element from the front of the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Nothing to delete.")
        else:
            removed_data = self.front.data
            self.front = self.front.next  # Move front to the next node
            if self.front is None:  # If the queue is now empty, rear should also be None
                self.rear = None
            print(f"Deleted element: {removed_data}")

    # Peek operation to view the front element without removing it
    def peek(self):
        if self.is_empty():
            print("Queue is empty. No front element.")
        else:
            print(f"Front element: {self.front.data}")

    # Traverse operation to display all elements in the queue
    def traverse(self):
        if self.is_empty():
            print("Queue is empty. Nothing to display.")
        else:
            print("Queue elements (front to rear):")
            current = self.front
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")  # Indicate the end of the queue

# Menu-driven program for queue operations
queue = Queue()

while True:
    print("\n!!! QUEUE OPERATIONS USING LINKED LIST !!!")
    print("1. INSERT (Enqueue)")
    print("2. DELETE (Dequeue)")
    print("3. PEEK (Front Element)")
    print("4. TRAVERSE (Display Queue)")
    print("0. EXIT")

    # User's choice
    choice = int(input("Enter your choice: "))

    if choice == 1:  # Enqueue
        value = int(input("Enter value to insert: "))
        queue.enqueue(value)

    elif choice == 2:  # Dequeue
        queue.dequeue()

    elif choice == 3:  # Peek
        queue.peek()

    elif choice == 4:  # Traverse
        queue.traverse()

    elif choice == 0:  # Exit
        print("Exiting... Bye!")
        break

    else:  # Invalid choice
        print("Invalid choice. Please try again.")

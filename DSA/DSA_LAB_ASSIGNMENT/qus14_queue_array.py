# Queue implementation using an array
class Queue:
    def __init__(self, capacity):
        self.queue = []  # Initialize the queue as an empty list
        self.capacity = capacity  # Set the maximum capacity of the queue

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Check if the queue is full
    def is_full(self):
        return len(self.queue) == self.capacity

    # Enqueue operation to insert an element into the queue
    def enqueue(self, data):
        if self.is_full():
            print("Queue is full. Cannot insert more elements.")
        else:
            self.queue.append(data)  # Add the element to the end of the list
            print(f"{data} inserted into the queue.")

    # Dequeue operation to remove an element from the front of the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Nothing to delete.")
        else:
            removed_item = self.queue.pop(0)  # Remove the first element from the list
            print(f"Deleted element: {removed_item}")

    # Peek operation to view the front element of the queue
    def peek(self):
        if self.is_empty():
            print("Queue is empty. No front element.")
        else:
            print(f"Front element: {self.queue[0]}")

    # Traverse operation to display all elements in the queue
    def traverse(self):
        if self.is_empty():
            print("Queue is empty. Nothing to display.")
        else:
            print("Queue elements:")
            for item in self.queue:
                print(item, end=" ")
            print()  # Add a new line after printing all elements

# Menu-driven program for queue operations
capacity = int(input("Enter the capacity of the queue: "))
queue = Queue(capacity)

while True:
    print("\n!!! QUEUE OPERATIONS USING ARRAY !!!")
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

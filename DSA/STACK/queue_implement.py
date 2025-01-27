class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{data} enqueued successfully.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Nothing to dequeue.")
            return
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"{dequeued_data} dequeued successfully.")

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print(f"Front of Queue: {self.front.data}")

    def traverse(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements are:")
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def is_empty(self):
        return self.front is None

# Menu-driven program
if __name__ == "__main__":
    queue = Queue()

    while True:
        print("\n--- Queue Operations ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Traverse")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter data to enqueue: "))
            queue.enqueue(data)
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.peek()
        elif choice == 4:
            queue.traverse()
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")

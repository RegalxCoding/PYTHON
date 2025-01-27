import threading

# Shared list of numbers
numbers = [1, 2, 3, 4, 5]

# Function to calculate the sum of numbers
def calculate_sum(numbers):
    total = sum(numbers)
    print(f"Sum of numbers: {total}")

# Function to calculate the product of numbers
def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    print(f"Product of numbers: {product}")

# Create threads
thread1 = threading.Thread(target=calculate_sum, args=(numbers,))
thread2 = threading.Thread(target=calculate_product, args=(numbers,))

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Calculation complete!")


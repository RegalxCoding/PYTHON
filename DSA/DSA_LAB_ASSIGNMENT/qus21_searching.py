def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    while True:
        print("\nSearch Program:")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            arr = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
            target = int(input("Enter the number to search for: "))
            index = linear_search(arr, target)
            if index != -1:
                print(f"Number found at index {index}.")
            else:
                print("Number not found.")

        elif choice == '2':
            arr = list(map(int, input("Enter the sorted list of numbers (space-separated): ").split()))
            target = int(input("Enter the number to search for: "))
            index = binary_search(arr, target)
            if index != -1:
                print(f"Number found at index {index}.")
            else:
                print("Number not found.")

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

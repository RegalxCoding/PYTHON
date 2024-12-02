# List of tuples
data = [
    ("Rushabh", 25),
    ("Rohan", 30),
    ("Aman", 20),
    ("Shivansh", 10)
]

# Sorting by the second element (age) using a lambda function
sorted_by_age = sorted(data, key=lambda x: x[1])

# Sorting by the first element (name) using a lambda function
sorted_by_name = sorted(data, key=lambda x: x[0])

# Print the results
print("Original list of tuples:")
print(data)

print("\nSorted by age (ascending):")
print(sorted_by_age)

print("\nSorted by name (alphabetical):")
print(sorted_by_name)

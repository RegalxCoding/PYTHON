# Algorithm to Delete Elements from Linked List Whose Sum is Zero
# 1.Traverse the List:

# Use a pointer to traverse the linked list.
# Maintain a dictionary (prefix_map) to store prefix sums and their corresponding nodes.
# 2.Calculate Prefix Sums:

# Start with prefix_sum = 0.
# For each node:
# Add the node's value to the prefix_sum.
# 3.Check for Zero Sum:

# If prefix_sum is 0, delete all nodes from the head up to the current node.
# If prefix_sum is found in the dictionary:
# Delete all nodes between the previous occurrence of the prefix_sum and the current node.
# 4.Update Pointers:

# Adjust the next pointer of the node before the range to skip the nodes in the range.
# 5.Continue Until End of List:

# Repeat the process for all nodes.

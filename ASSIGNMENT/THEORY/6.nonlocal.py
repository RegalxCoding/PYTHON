def outer_function():
    # Outer function variable
    count = 0

    def inner_function():
        nonlocal count  # Declare count as nonlocal to modify the outer variable
        count += 1
        print(f"Inner function called. Updated count: {count}")

    print(f"Initial count: {count}")
    inner_function()
    inner_function()
    inner_function()
    print(f"Final count: {count}")

# Call the outer function
outer_function()

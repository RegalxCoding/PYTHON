row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

arr = []

# Input elements into the matrix
for i in range(row):
    row_element = []
    for j in range(col):
        element = int(input(f"Enter element ({i}, {j}): "))
        row_element.append(element)
    arr.append(row_element)

# Display the matrix
print("\nMATRIX\n")
for i in range(row):
    for j in range(col):
        print(arr[i][j], end="\t")
    print()

# Count non-zero and zero elements
nz, z = 0, 0
for i in range(row):
    for j in range(col):
        if arr[i][j] != 0:
            nz += 1
        else:
            z += 1

# Determine if the matrix is sparse or not
if nz > z:
    print("\nMATRIX IS NOT A SPARSE MATRIX\n")
else:
    sm = []
    for i in range(row):
        for j in range(col):
            if arr[i][j] != 0:
                sm.append([i, j, arr[i][j]])

    # Display sparse matrix
    print("\nSPARSE MATRIX\n")
    print("row\tcol\tvalue")
    for row in sm:
        print(row[0], row[1], row[2], sep="\t")

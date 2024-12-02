#!!!!!JUST ALOGIRTHM NOT CODE !!!!!!
# Algorithm for Adding Two Sparse Matrices
# 1.Input Matrices: Read the dimensions and elements of the two matrices.
# 2.Validate Dimensions: Ensure both matrices have the same dimensions; otherwise, matrix addition is not possible.
# 3.Convert to Sparse Representation: Convert both matrices into their sparse representations (a list of [row, col, value] for non-zero elements).
# 4.Add Sparse Matrices:
# 5.Traverse both sparse representations.
# 6.If the positions match, add their values.
# 7.If one matrix has a non-zero value at a position while the other doesn't, include the non-zero value in the result.
# 8.Output Result: Convert the result back to matrix form or display it in sparse format.
# Input a matrix and return it as a 2D list
def input_matrix(row, col):
    matrix = []
    print("\nEnter the elements of the matrix:")
    for i in range(row):
        row_elements = []
        for j in range(col):
            element = int(input(f"Element at ({i}, {j}): "))
            row_elements.append(element)
        matrix.append(row_elements)
    return matrix

# Convert a matrix to its sparse representation
def to_sparse(matrix):
    sparse_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                sparse_matrix.append([i, j, matrix[i][j]])
    return sparse_matrix

# Add two sparse matrices
def add_sparse_matrices(sparse1, sparse2):
    result = []
    i = j = 0

    while i < len(sparse1) and j < len(sparse2):
        if sparse1[i][:2] == sparse2[j][:2]:
            # Same row and column indices, add values
            result.append([sparse1[i][0], sparse1[i][1], sparse1[i][2] + sparse2[j][2]])
            i += 1
            j += 1
        elif sparse1[i][:2] < sparse2[j][:2]:
            # Take element from sparse1
            result.append(sparse1[i])
            i += 1
        else:
            # Take element from sparse2
            result.append(sparse2[j])
            j += 1

    # Add remaining elements from both sparse matrices
    result.extend(sparse1[i:])
    result.extend(sparse2[j:])

    return result

# Display a matrix
def display_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))

# Main Program
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

# Input two matrices
print("\nMatrix 1:")
matrix1 = input_matrix(row, col)
print("\nMatrix 2:")
matrix2 = input_matrix(row, col)

# Display the input matrices
print("\nMatrix 1:")
display_matrix(matrix1)
print("\nMatrix 2:")
display_matrix(matrix2)

# Convert to sparse representations
sparse1 = to_sparse(matrix1)
sparse2 = to_sparse(matrix2)

# Add sparse matrices
sparse_sum = add_sparse_matrices(sparse1, sparse2)

# Display the sparse sum
print("\nSparse Matrix Representation of Sum:")
print("Row\tCol\tValue")
for row in sparse_sum:
    print("\t".join(map(str, row)))

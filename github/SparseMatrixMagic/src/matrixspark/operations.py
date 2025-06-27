# Imports the Matrix class from the core module to use its functionality in matrix operations.
from core import Matrix


# Defines a function to compute the determinant of a square matrix.
def compute_determinant(matrix):
    # Checks if the matrix is square by comparing the number of rows and columns.
    if matrix.rows != matrix.cols:
        # Raises a ValueError if the matrix is not square, as determinant is only defined for square matrices.
        raise ValueError("Determinant is only defined for square matrices.")
    # Handles the base case where the matrix is 1x1.
    if matrix.rows == 1:
        # Returns the single element of a 1x1 matrix as its determinant.
        return matrix[0, 0]
    # Initializes the determinant value to 0.
    det = 0
    # Iterates over each column index in the first row to compute the determinant using cofactor expansion.
    for j in range(matrix.cols):
        # Checks if the element at position (0, j) is non-zero to avoid unnecessary computations.
        if matrix[0, j] != 0:
            # Computes the cofactor for the element at position (0, j).
            cofactor = compute_cofactor(matrix, 0, j)
            # Adds the contribution of the element to the determinant: (-1)^j * element * cofactor.
            det += ((-1) ** j) * matrix[0, j] * cofactor
    # Returns the computed determinant value.
    return det


# Defines a function to compute the cofactor for a specific element at position (row, col) in the matrix.
def compute_cofactor(matrix, row, col):
    # Creates a new Matrix instance for the submatrix, with dimensions reduced by 1 (excluding the specified row and column).
    submatrix = Matrix(matrix.rows - 1, matrix.cols - 1)
    # Iterates over all row indices of the original matrix.
    for i in range(matrix.rows):
        # Skips the row that is to be excluded for the cofactor computation.
        if i == row:
            # Continues to the next iteration, ignoring this row.
            continue
        # Iterates over all column indices of the original matrix.
        for j in range(matrix.cols):
            # Skips the column that is to be excluded for the cofactor computation.
            if j == col:
                # Continues to the next iteration, ignoring this column.
                continue
            # Computes the row index for the submatrix (adjusts if i is after the excluded row).
            sub_i = i if i < row else i - 1
            # Computes the column index for the submatrix (adjusts if j is after the excluded column).
            sub_j = j if j < col else j - 1
            # Checks if the element at (i, j) exists in the original matrix's data dictionary.
            if (i, j) in matrix.data:
                # Copies the element from the original matrix to the appropriate position in the submatrix.
                submatrix[sub_i, sub_j] = matrix[i, j]
    # Returns the determinant of the submatrix, which is the cofactor value.
    return submatrix.determinant


# Defines a function to compute the transpose of a matrix.
def compute_transpose(matrix):
    # Creates a new Matrix instance for the transpose, with swapped dimensions (rows become columns, columns become rows).
    transpose = Matrix(matrix.cols, matrix.rows)
    # Iterates over all non-zero elements in the original matrix's data dictionary.
    for (i, j), value in matrix.data.items():
        # Sets the element at position (j, i) in the transpose matrix to the value at (i, j) in the original matrix.
        transpose[j, i] = value
    # Returns the transposed matrix.
    return transpose


# Defines a function to add two matrices of the same dimensions.
def add_matrices(a, b):
    # Checks if the dimensions of both matrices match (same number of rows and columns).
    if a.rows != b.rows or a.cols != b.cols:
        # Raises a ValueError if the dimensions do not match, as addition requires identical dimensions.
        raise ValueError("Matrix dimensions must match for addition.")
    # Creates a new Matrix instance for the result, with the same dimensions as the input matrices.
    result = Matrix(a.rows, a.cols)
    # Iterates over all non-zero elements in the first matrix's data dictionary.
    for (i, j), value in a.data.items():
        # Copies the element from the first matrix to the result matrix at the same position.
        result[i, j] = value
    # Iterates over all non-zero elements in the second matrix's data dictionary.
    for (i, j), value in b.data.items():
        # Adds the element from the second matrix to the existing value in the result matrix at position (i, j).
        result[i, j] = result[i, j] + value
    # Returns the resulting matrix, which is the sum of the two input matrices.
    return result


# Defines a function to perform element-wise multiplication of two matrices.
def elementwise_multiply(a, b):
    # Checks if the dimensions of both matrices match (same number of rows and columns).
    if a.rows != b.rows or a.cols != b.cols:
        # Raises a ValueError if the dimensions do not match, as element-wise multiplication requires identical dimensions.
        raise ValueError("Matrix dimensions must match for element-wise multiplication.")
    # Creates a new Matrix instance for the result, with the same dimensions as the input matrices.
    result = Matrix(a.rows, a.cols)
    # Iterates over all non-zero elements in the first matrix's data dictionary.
    for (i, j), value in a.data.items():
        # Checks if the second matrix has a non-zero element at the same position (i, j).
        if (i, j) in b.data:
            # Sets the result at (i, j) to the product of the elements from both matrices at that position.
            result[i, j] = value * b[i, j]
    # Returns the resulting matrix, containing products of corresponding elements where both are non-zero.
    return result


# Defines a function to perform matrix multiplication (matmul) of two matrices.
def matmul(a, b):
    # Checks if the number of columns in matrix a matches the number of rows in matrix b, as required for matrix multiplication.
    if a.cols != b.rows:
        # Raises a ValueError if the dimensions are incompatible for matrix multiplication.
        raise ValueError("Matrix A's columns must match Matrix B's rows for multiplication.")
    # Creates a new Matrix instance for the result, with rows from matrix a and columns from matrix b.
    result = Matrix(a.rows, b.cols)
    # Iterates over all non-zero elements in matrix a's data dictionary.
    for (i, j), a_val in a.data.items():
        # Iterates over all column indices of the result matrix (columns of matrix b).
        for k in range(b.cols):
            # Iterates over the row indices of matrix b (which correspond to columns of matrix a).
            for m in range(b.rows):
                # Checks if matrix b has a non-zero element at position (m, k).
                if (m, k) in b.data:
                    # Adds the product of a[i, j] and b[m, k] to the result at position (i, k).
                    result[i, k] = result[i, k] + a_val * b[m, k]
    # Returns the resulting matrix, which is the product of matrices a and b.
    return result
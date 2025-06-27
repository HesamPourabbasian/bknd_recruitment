# Imports the Matrix class from the core module to create and manipulate sparse matrices.
from core import Matrix
# Imports matrix operation functions (add_matrices, elementwise_multiply, matmul) from the operations module.
from operations import add_matrices, elementwise_multiply, matmul
# Imports the pretty_print function from the utils module for formatted matrix output.
from utils import pretty_print
# Imports Fore and Style from the colorama library to enable colored and styled terminal output.
from colorama import Fore, Style

# Creates a 3x3 Matrix instance A with specified non-zero elements stored in a dictionary.
A = Matrix(3, 3, {(0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 7, (2, 1): 8, (2, 2): 9})
# Creates a 3x3 Matrix instance B with specified non-zero elements stored in a dictionary.
B = Matrix(3, 3, {(0, 0): 9, (0, 1): 8, (0, 2): 7, (1, 0): 6, (1, 1): 5, (1, 2): 4, (2, 0): 3, (2, 1): 2, (2, 2): 1})

# Computes the sum of matrices A and B using the add_matrices function and stores the result in C.
C = add_matrices(A, B)
# Prints matrix C with a title "A + B:" in green color using the pretty_print function.
pretty_print(C, "A + B:", Fore.GREEN)

# Computes the element-wise product of matrices A and B using the elementwise_multiply function and stores the result in D.
D = elementwise_multiply(A, B)
# Prints matrix D with a title "A * B (element-wise):" in red color using the pretty_print function.
pretty_print(D, "A * B (element-wise):", Fore.RED)

# Computes the matrix product (dot product) of matrices A and B using the matmul function and stores the result in E.
E = matmul(A, B)
# Prints matrix E with a title "A @ B (dot product):" in blue color using the pretty_print function.
pretty_print(E, "A @ B (dot product):", Fore.BLUE)

# Prints the determinant of matrix A in cyan color, accessing the determinant property and resetting the style afterward.
print(f"\n{Fore.CYAN}Determinant of A: {A.determinant}{Style.RESET_ALL}")

# Prints the transpose of matrix A with a title "Transpose of A:" in magenta color using the pretty_print function.
pretty_print(A.transpose, "Transpose of A:", Fore.MAGENTA)

# Defines a vector as a list for matrix-vector multiplication.
vector = [1, 2, 3]
# Performs matrix-vector multiplication by calling matrix A with the vector and stores the result.
result = A(vector)
# Prints the result of the matrix-vector multiplication in yellow color, including the input vector and resetting the style.
print(f"\n{Fore.YELLOW}Matrix-vector multiplication A * {vector}: {result}{Style.RESET_ALL}")
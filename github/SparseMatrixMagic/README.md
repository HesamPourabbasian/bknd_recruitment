Matrix Operations Library 🧮✨
Welcome to the Matrix Operations Library, a sleek and efficient Python project designed for performing matrix computations with elegance and ease! 🚀 This library leverages a sparse matrix implementation to handle operations like addition, multiplication, determinants, transposes, and more, all wrapped in a visually appealing output powered by colorama. Perfect for math enthusiasts, students, or developers looking to dive into linear algebra with style! 🌟

## Features ##

Sparse Matrix Representation 📊: Efficiently stores only non-zero elements to save memory and boost performance.
Core Operations 🔢:
Matrix addition ➕
Element-wise multiplication ✖️
Matrix multiplication (dot product) 🔄
Determinant calculation 📈
Matrix transpose 🔃
Matrix-vector multiplication 🚀


Beautiful Output 🎨: Uses colorama to print matrices with vibrant, color-coded formatting for clear visualization.
Caching for Performance ⚡: Caches determinant and transpose results to avoid redundant computations.
Error Handling 🛡️: Robust checks for matrix dimensions and valid inputs to ensure reliable operations.

🛠️ How It Works
The library is built around a Matrix class (in core.py) that uses a dictionary to store non-zero elements, making it ideal for sparse matrices. Operations are modularized across files for clarity and reusability:

core.py 🧱: Defines the Matrix class with methods for element access, iteration, and dynamic properties like determinant and transpose.
Operations (operations.py) 🔧:
add_matrices: Adds two matrices of the same size.
elementwise_multiply: Performs element-wise multiplication.
matmul: Computes the matrix dot product.
compute_determinant: Calculates the determinant using cofactor expansion.
compute_cofactor: Computes cofactors for determinant calculations.
compute_transpose: Generates the transpose of a matrix.


Utilities (utils.py) 🖌️: Includes pretty_print for formatted, colorful matrix output using colorama.
Main Script (main.py) 🎮: Demonstrates the library’s capabilities with example matrices, showcasing addition, multiplication, determinant, transpose, and matrix-vector operations with vibrant terminal output.

🎉 Example Usage
The main script creates two 3x3 matrices and performs various operations, printing the results in a visually stunning format:
````
Matrix A:
┌───────┐
│ 1 2 3 │
│ 4 5 6 │
│ 7 8 9 │
└───────┘


Matrix B:
┌───────┐
│ 9 8 7 │
│ 6 5 4 │
│ 3 2 1 │
└───────┘
````

Operations:

Addition (A + B): Displayed in green.
Element-wise Multiplication (A * B): Displayed in red.
Matrix Multiplication (A @ B): Displayed in blue.
Determinant of A: Printed in cyan.
Transpose of A: Displayed in magenta.
Matrix-Vector Multiplication (A * [1, 2, 3]): Printed in yellow.



The output is not only functional but also a delight to look at, making matrix operations both understandable and fun! 😄
🧑‍💻 Who Is This For?

Students 📚: Learning linear algebra and wanting to visualize matrix operations.
Developers 💻: Building applications that require efficient matrix computations.
Math Enthusiasts 🧠: Exploring the beauty of matrices with a practical, hands-on tool.
Anyone 🌍: Curious about combining Python, math, and colorful terminal art!


📂 Project Structure
````
matrix-library/
├── core.py           # Matrix class implementation
├── operations.py     # Matrix operation functions
├── utils.py          # Utility functions for printing
├── main.py           # Demo script showcasing operations
````
🎯 Get Started
Just run the main.py script to see the magic happen! Watch as matrices come to life in your terminal with colorful, well-formatted output. Experiment with your own matrices by modifying the script or extending the library with new features! 🛠️
Happy matrix computing! 🎉

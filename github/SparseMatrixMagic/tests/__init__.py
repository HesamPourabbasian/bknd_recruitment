import math
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init()


class Matrix:
    def __init__(self, rows, cols, values=None):
        self.rows = rows
        self.cols = cols
        self.data = values if values else {}  # Sparse matrix storage
        self._determinant_cache = None
        self._transpose_cache = None

    def __getitem__(self, idx):
        i, j = idx
        return self.data.get((i, j), 0)

    def __setitem__(self, idx, value):
        i, j = idx
        if value == 0:
            self.data.pop((i, j), None)  # Remove zero entries
        else:
            self.data[(i, j)] = value
        # Invalidate caches on modification
        self._determinant_cache = None
        self._transpose_cache = None

    def __iter__(self):
        for i in range(self.rows):
            yield [self[i, j] for j in range(self.cols)]

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition.")
        result = Matrix(self.rows, self.cols)
        for (i, j), value in self.data.items():
            result[i, j] = value
        for (i, j), value in other.data.items():
            result[i, j] = result[i, j] + value
        return result

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for element-wise multiplication.")
        result = Matrix(self.rows, self.cols)
        for (i, j), value in self.data.items():
            if (i, j) in other.data:
                result[i, j] = value * other[i, j]
        return result

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix A's columns must match Matrix B's rows for multiplication.")
        result = Matrix(self.rows, other.cols)
        for (i, j), a_val in self.data.items():
            for k in range(other.cols):
                for m in range(other.rows):
                    if (m, k) in other.data:
                        result[i, k] = result[i, k] + a_val * other[m, k]
        return result

    def __call__(self, vector):
        if not isinstance(vector, list) or len(vector) != self.cols:
            raise ValueError("Vector length must match matrix column count.")
        result = [0] * self.rows
        for (i, j), value in self.data.items():
            result[i] += value * vector[j]
        return result

    def __getattr__(self, name):
        if name == 'determinant':
            if self._determinant_cache is None:
                self._determinant_cache = self._compute_determinant()
            return self._determinant_cache
        elif name == 'transpose':
            if self._transpose_cache is None:
                self._transpose_cache = self._compute_transpose()
            return self._transpose_cache
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def _compute_determinant(self):
        if self.rows != self.cols:
            raise ValueError("Determinant is only defined for square matrices.")
        if self.rows == 1:
            return self[0, 0]
        det = 0
        for j in range(self.cols):
            if self[0, j] != 0:
                cofactor = self._compute_cofactor(0, j)
                det += ((-1) ** j) * self[0, j] * cofactor
        return det

    def _compute_cofactor(self, row, col):
        submatrix = Matrix(self.rows - 1, self.cols - 1)
        for i in range(self.rows):
            if i == row:
                continue
            for j in range(self.cols):
                if j == col:
                    continue
                sub_i = i if i < row else i - 1
                sub_j = j if j < col else j - 1
                if (i, j) in self.data:
                    submatrix[sub_i, sub_j] = self[i, j]
        return submatrix.determinant

    def _compute_transpose(self):
        transpose = Matrix(self.cols, self.rows)
        for (i, j), value in self.data.items():
            transpose[j, i] = value
        return transpose

    def pretty_print(self, title="", color=Fore.WHITE):
        """Prints the matrix in a neat, table-like format with color."""
        print(f"{color}{Style.BRIGHT}{title}{Style.RESET_ALL}")
        # Find the maximum width needed for any number
        max_width = max(
            len(str(int(self[i, j]))) for i in range(self.rows) for j in range(self.cols)
        ) or 1
        # Top border
        print(f"{color}┌{'─' * (max_width + 2) * self.cols}┐{Style.RESET_ALL}")
        # Matrix rows
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                value = int(self[i, j])  # Convert to int for clean display
                row.append(f"{value:>{max_width}}")
            print(f"{color}│ {' '.join(row)} │{Style.RESET_ALL}")
        # Bottom border
        print(f"{color}└{'─' * (max_width + 2) * self.cols}┘{Style.RESET_ALL}")


# Test the code
A = Matrix(3, 3, {(0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 7, (2, 1): 8, (2, 2): 9})
B = Matrix(3, 3, {(0, 0): 9, (0, 1): 8, (0, 2): 7, (1, 0): 6, (1, 1): 5, (1, 2): 4, (2, 0): 3, (2, 1): 2, (2, 2): 1})

# Matrix addition
C = A + B
C.pretty_print("A + B:", Fore.GREEN)

# Matrix multiplication (element-wise)
D = A * B
D.pretty_print("\nA * B (element-wise):", Fore.RED)

# Matrix multiplication (dot product)
E = A @ B
E.pretty_print("\nA @ B (dot product):", Fore.BLUE)

# Matrix determinant (cached)
print(f"\n{Fore.CYAN}Determinant of A: {A.determinant}{Style.RESET_ALL}")

# Matrix transpose (cached)
A.transpose.pretty_print("\nTranspose of A:", Fore.MAGENTA)

# Matrix-vector multiplication
vector = [1, 2, 3]
result = A(vector)
print(f"\n{Fore.YELLOW}Matrix-vector multiplication A * {vector}: {result}{Style.RESET_ALL}")

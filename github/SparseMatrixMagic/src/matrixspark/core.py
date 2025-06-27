# Defines a Matrix class to represent a sparse matrix using a dictionary for non-zero elements.
class Matrix:
    # Constructor method to initialize a Matrix instance.
    def __init__(self, rows, cols, values=None):
        # Stores the number of rows in the matrix as an instance variable.
        self.rows = rows
        # Stores the number of columns in the matrix as an instance variable.
        self.cols = cols
        # Initializes the data dictionary to store non-zero elements; uses provided values if given, otherwise an empty dictionary.
        self.data = values if values else {}
        # Initializes a cache for the determinant as None, to be computed later if needed.
        self._determinant_cache = None
        # Initializes a cache for the transpose as None, to be computed later if needed.
        self._transpose_cache = None

    # Defines how to access matrix elements using indexing (e.g., matrix[i, j]).
    def __getitem__(self, idx):
        # Unpacks the index tuple into row (i) and column (j) indices.
        i, j = idx
        # Returns the value at position (i, j) from the data dictionary, defaulting to 0 if not found (sparse matrix convention).
        return self.data.get((i, j), 0)

    # Defines how to set matrix elements using indexing (e.g., matrix[i, j] = value).
    def __setitem__(self, idx, value):
        # Unpacks the index tuple into row (i) and column (j) indices.
        i, j = idx
        # If the value is 0, removes the entry from the data dictionary (sparse matrix stores only non-zero elements).
        if value == 0:
            # Removes the key (i, j) from the data dictionary if it exists, does nothing if it doesn't.
            self.data.pop((i, j), None)
        # If the value is non-zero, stores it in the data dictionary at key (i, j).
        else:
            # Assigns the value to the key (i, j) in the data dictionary.
            self.data[(i, j)] = value
        # Invalidates the determinant cache since the matrix has changed.
        self._determinant_cache = None
        # Invalidates the transpose cache since the matrix has changed.
        self._transpose_cache = None

    # Defines how the matrix can be iterated over, yielding rows as lists.
    def __iter__(self):
        # Loops through each row index from 0 to rows-1.
        for i in range(self.rows):
            # Yields a list representing row i, with elements accessed via __getitem__ for columns 0 to cols-1.
            yield [self[i, j] for j in range(self.cols)]

    # Defines the behavior when the matrix is called as a function, e.g., matrix(vector), for matrix-vector multiplication.
    def __call__(self, vector):
        # Checks if the input is a list and its length matches the number of matrix columns.
        if not isinstance(vector, list) or len(vector) != self.cols:
            # Raises a ValueError if the vector is invalid or has incorrect length.
            raise ValueError("Vector length must match matrix column count.")
        # Initializes a result list of zeros with length equal to the number of rows.
        result = [0] * self.rows
        # Iterates over each non-zero element in the data dictionary, with (i, j) as the position and value as the element.
        for (i, j), value in self.data.items():
            # Updates the i-th element of the result by adding the product of the matrix element and the j-th vector element.
            result[i] += value * vector[j]
        # Returns the resulting vector from the matrix-vector multiplication.
        return result

    # Defines custom attribute access for dynamic properties like determinant and transpose.
    def __getattr__(self, name):
        # Imports compute_determinant and compute_transpose functions from the operations module when needed.
        from operations import compute_determinant, compute_transpose
        # Checks if the requested attribute is 'determinant'.
        if name == 'determinant':
            # If the determinant cache is None, computes the determinant and stores it in the cache.
            if self._determinant_cache is None:
                # Calls compute_determinant to calculate the determinant and caches the result.
                self._determinant_cache = compute_determinant(self)
            # Returns the cached determinant value.
            return self._determinant_cache
        # Checks if the requested attribute is 'transpose'.
        elif name == 'transpose':
            # If the transpose cache is None, computes the transpose and stores it in the cache.
            if self._transpose_cache is None:
                # Calls compute_transpose to calculate the transpose and caches the result.
                self._transpose_cache = compute_transpose(self)
            # Returns the cached transpose matrix.
            return self._transpose_cache
        # If the attribute name is neither 'determinant' nor 'transpose', raises an AttributeError.
        else:
            # Raises an AttributeError with a message indicating the attribute doesn't exist.
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
# Imports Fore and Style from the colorama library to enable colored and styled terminal output.
from colorama import Fore, Style


# Defines a function to print a matrix in a visually appealing format with optional title and color.
def pretty_print(matrix, title="", color=Fore.WHITE):
    # Prints the title with the specified color and bright style, resetting the style afterward.
    print(f"{color}{Style.BRIGHT}{title}{Style.RESET_ALL}")
    # Calculates the maximum width needed for any matrix element (converted to integer) to ensure aligned formatting.
    max_width = max(
        # Computes the length of the string representation of each matrix element (as an integer).
        len(str(int(matrix[i, j]))) for i in range(matrix.rows) for j in range(matrix.cols)
    ) or 1  # Defaults to 1 if no elements exist or all are zero.
    # Prints the top border of the matrix, using the specified color, with width adjusted for elements and spacing.
    print(f"{color}┌{'─' * (max_width + 2) * matrix.cols}┐{Style.RESET_ALL}")
    # Iterates over each row index of the matrix.
    for i in range(matrix.rows):
        # Initializes an empty list to store formatted elements of the current row.
        row = []
        # Iterates over each column index of the matrix for the current row.
        for j in range(matrix.cols):
            # Converts the matrix element at (i, j) to an integer for display.
            value = int(matrix[i, j])
            # Formats the value as a string, right-aligned to the maximum width, and adds it to the row list.
            row.append(f"{value:>{max_width}}")
        # Prints the row, with elements joined by spaces, enclosed in vertical bars, using the specified color.
        print(f"{color}│ {' '.join(row)} │{Style.RESET_ALL}")
    # Prints the bottom border of the matrix, matching the top border, using the specified color.
    print(f"{color}└{'─' * (max_width + 2) * matrix.cols}┘{Style.RESET_ALL}")
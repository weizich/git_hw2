def parse_matrix(input_str):
    """
    Parse the input string to create a matrix dictionary.
    Args:
    input_str (str): The input string representing the matrix.
    
    Returns:
    dict: The matrix represented as a dictionary with (row, col) as keys.
    int: The size of the matrix.
    """
    matrix = {}
    rows = input_str.strip().split('|')
    n = len(rows)
    
    for i, row in enumerate(rows):
        elements = row.split(',')
        if len(elements) != n:
            raise ValueError("Number of columns in a row does not match the specified size n")
        for j, value in enumerate(elements):
            try:
                matrix[(i, j)] = int(value)
            except ValueError:
                raise ValueError(f"Invalid integer value at row {i+1}, column {j+1}")
    
    return matrix, n

def matrix_multiplication(U, V, n):
    """
    Perform matrix multiplication on two n x n matrices.
    Args:
    U (dict): The first matrix.
    V (dict): The second matrix.
    n (int): The size of the matrices.
    
    Returns:
    dict: The resulting matrix of the multiplication.
    """
    M = {}
    for i in range(n):
        for j in range(n):
            M[(i, j)] = 0
            for k in range(n):
                M[(i, j)] += U.get((i, k), 0) * V.get((k, j), 0)
    return M

def print_matrix(matrix, n):
    """
    Print the matrix in a readable format.
    Args:
    matrix (dict): The matrix to be printed.
    n (int): The size of the matrix.
    """
    for i in range(n):
        row = [str(matrix.get((i, j), 0)) for j in range(n)]
        print(f"[{', '.join(row)}]")

def main():
    # Input the matrices in the specified format
    U_str = input("Enter matrix U: ")
    V_str = input("Enter matrix V: ")
    
    try:
        # Parse the input strings to create matrix dictionaries
        U, n = parse_matrix(U_str)
        V, _ = parse_matrix(V_str)
    except ValueError as e:
        print(f"Error parsing matrices: {e}")
        return
    
    # Compute the resulting matrix M = U * V
    M = matrix_multiplication(U, V, n)
    
    # Print the resulting matrix
    print("M = U x V")
    print_matrix(M, n)

if __name__ == "__main__":
    main()

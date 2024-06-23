size = int(input("Enter the size of the grid: "))

# construct a 2-d matrix with dimension n
matrix = [["_" for i in range(size)] for j in range(size)]

for i in range(size):
        print(" ".join(matrix[i]))

cell_coordinate = ""
new_value = ""

while True:
    cell_coordinate = input("Enter the cell coordinates to edit: ")
    if cell_coordinate == "done":
        break
    else:
        row, col = cell_coordinate.split(",")
        row, col = int(row), int(col)
    new_value = input("Enter the new value for the cell: ")

    # update the matrix value
    matrix[row][col] = new_value

    for i in range(size):
        print(" ".join(matrix[i]))

# 從使用者輸入目標位置和目標顏色
input_data = input("Enter index x,y,k (separated by whitespace): ").split()
target_x, target_y, target_color = int(input_data[0]), int(input_data[1]), int(input_data[2])

# 從使用者輸入獲取矩陣，直到輸入 'q' 為止
matrix = []
print("Enter the matrix by multiple lines:")
while True:
    row = input()
    if row.lower() == 'q':
        break
    matrix.append([int(x) for x in row.split()])

# 預設使用者輸入的顏色一定與原本顏色不一樣
original_color = matrix[target_x][target_y]

# 使用深度優先搜索（DFS）進行泛洪填充
stack = [(target_x, target_y)]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
while stack:
    x, y = stack.pop()
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == original_color:
        matrix[x][y] = target_color
        for dx, dy in directions:
            stack.append((x + dx, y + dy))

print("替換後的矩陣:")
for row in matrix:
    print(' '.join(str(x) for x in row))

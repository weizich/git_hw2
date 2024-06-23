import random

# 生成从起点到终点的路径
def generate_path(maze, N, M):
    r, c = 0, 0
    while r < N - 1 or c < M - 1:
        maze[(r, c)] = 2
        if r < N - 1 and (c == M - 1 or random.choice([True, False])):
            r += 1
        elif c < M - 1:
            c += 1
    maze[(r, c)] = 2  # 将终点标记为路径的一部分

# 添加随机障碍物
def add_obstacles(maze, min_obstacles, N, M):
    empty_cells = [(r, c) for r in range(N) for c in range(M) if maze.get((r, c), 0) == 0]
    random.shuffle(empty_cells)
    count = 0
    while count < min_obstacles and empty_cells:
        r, c = empty_cells.pop()
        if maze.get((r, c), 0) == 0:
            maze[(r, c)] = 1
            count += 1

# 手动设置障碍物
def set_obstacle(maze, N, M):
    try:
        r = int(input("Enter the row to add obstacle: "))
        c = int(input("Enter the column to add obstacle: "))
        if r < 0 or r >= N or c < 0 or c >= M:
            raise KeyError
        if maze.get((r, c), 0) == 2:
            print("Error: Cannot set obstacle on the path.")
        else:
            maze[(r, c)] = 1
            print_maze(maze, N, M)
    except ValueError:
        print("Error: Input must be an integer.")
    except KeyError:
        print("Error: Coordinates out of bounds.")

# 手动移除障碍物
def remove_obstacle(maze, N, M):
    try:
        r = int(input("Enter the row to remove obstacle: "))
        c = int(input("Enter the column to remove obstacle: "))
        if r < 0 or r >= N or c < 0 or c >= M:
            raise KeyError
        if maze.get((r, c), 0) != 1:
            print("Error: No obstacle at given cell.")
        else:
            maze[(r, c)] = 0
            print_maze(maze, N, M)
    except ValueError:
        print("Error: Input must be an integer.")
    except KeyError:
        print("Error: Coordinates out of bounds.")

# 打印当前迷宫状态
def print_maze(maze, N, M):
    for r in range(N):
        row = ""
        for c in range(M):
            cell = maze.get((r, c), 0)
            if cell == 0:
                row += "+---"  # 水平边
            elif cell == 1:
                row += "| X "  # 障碍物
            elif cell == 2:
                row += "| O "  # 路径
        print(row + "+")  # 边界
        if r < N - 1:
            row = ""
            for c in range(M):
                cell = maze.get((r, c), 0)
                if cell == 0:
                    row += "|   "  # 垂直边
                elif cell == 1:
                    row += "| X "  # 障碍物
                elif cell == 2:
                    row += "| O "  # 路径
            print(row + "|")  # 边界

# 主函数
def main():
    while True:
        try:
            filename = input("Enter the filename of the maze blueprint: ")
            print(f"Trying to open file: {filename}")  # 调试信息
            with open(filename, 'r') as file:
                lines = file.readlines()
            break
        except Exception as e:  # 捕获所有异常
            print(f"Error: {e}")
            print("File not found or could not be read, please enter a valid filename.")
    
    N, M = len(lines), len(lines[0].strip())
    maze = {}
    
    for r, line in enumerate(lines):
        for c, char in enumerate(line.strip()):
            if char in '01':
                maze[(r, c)] = int(char)
    
    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles to add: "))
            if min_obstacles < 0:
                raise ValueError
            break
        except ValueError:
            print("Error: Please enter a valid positive integer.")

    generate_path(maze, N, M)
    add_obstacles(maze, min_obstacles, N, M)
    print_maze(maze, N, M)
    
    while True:
        print("Menu:")
        print("1. Add obstacle")
        print("2. Remove obstacle")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            set_obstacle(maze,N, M)
        elif choice == "2":
            remove_obstacle(maze, N, M)
        elif choice == "3":
            break
        else:
            print("Error: Invalid choice, please try again.")

if __name__ == "__main__":
    main()


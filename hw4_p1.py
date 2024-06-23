import random

def initialize_board():
    return [[' ' for _ in range(9)] for _ in range(9)]

def place_mines(board):
    mines = set()
    first_safe_cell = (random.randint(0, 8), random.randint(0, 8))
    mines.add(first_safe_cell)
    while len(mines) < 10:
        mine = (random.randint(0, 8), random.randint(0, 8))
        if mine != first_safe_cell:
            mines.add(mine)
    for mine in mines:
        board[mine[1]][mine[0]] = '*'
    return mines

def update_adjacent_numbers(board, mines):
    for i in range(9):
        for j in range(9):
            if board[i][j] != '*':
                count = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if (0 <= i + dx < 9 and 0 <= j + dy < 9 and
                                (i + dx, j + dy) in mines):
                            count += 1
                if count > 0:
                    board[i][j] = str(count)

def display_board(board):
    print('+-------+')
    for i in range(9):
        print('|' + '|'.join(board[i]) + '|')
    print('+-------+')

def unfold_cell(board, mines, x, y):
    if board[y][x] == ' ':
        board[y][x] = '0'
        if (x, y) not in mines:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 <= x + dx < 9 and 0 <= y + dy < 9:
                        unfold_cell(board, mines, x + dx, y + dy)

def check_win(board, mines, flags):
    uncovered = set()
    for i in range(9):
        for j in range(9):
            if board[j][i] != ' ':
                uncovered.add((i, j))
    return uncovered == set([(x, y) for x in range(9) for y in range(9)]) - mines

def play_game():
    board = initialize_board()
    mines = place_mines(board)
    update_adjacent_numbers(board, mines)
    display_board(board)
    flags = set()
    while True:
        choice = input("Enter cell label to unfold/flag (e.g., a5, Flag: f5): ").lower()
        if choice.startswith('f'):
            cell = (ord(choice[1]) - ord('a'), int(choice[2]) - 1)
            if cell not in flags:
                flags.add(cell)
                board[cell[1]][cell[0]] = 'F'
                display_board(board)
            else:
                print("Cell already flagged!")
        else:
            cell = (ord(choice[0]) - ord('a'), int(choice[1]) - 1)
            if cell in mines:
                print("Game Over! You hit a mine!")
                break
            else:
                unfold_cell(board, mines, cell[0], cell[1])
                display_board(board)
                if check_win(board, mines, flags):
                    print("Congratulations! You cleared the board!")
                    break

# Main
if __name__ == "__main__":
    play_game()
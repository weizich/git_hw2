import random
import os
import time

# 定義遊戲畫面大小
WIDTH = 20
HEIGHT = 10

# 定義遊戲物件符號
SNAKE_HEAD = 'O'
SNAKE_BODY = 'o'
FOOD = '*'

# 定義遊戲狀態
class GameState:
    def __init__(self):
        self.snake = [(5, 5)]
        self.food = self.generate_food()
        self.direction = 'RIGHT'
        self.score = 0
        self.game_over = False

    def generate_food(self):
        while True:
            food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
            if food not in self.snake:
                return food

    def move_snake(self):
        head = self.snake[0]
        if self.direction == 'UP':
            new_head = (head[0], head[1] - 1)
        elif self.direction == 'DOWN':
            new_head = (head[0], head[1] + 1)
        elif self.direction == 'LEFT':
            new_head = (head[0] - 1, head[1])
        elif self.direction == 'RIGHT':
            new_head = (head[0] + 1, head[1])

        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            self.game_over = True
            return

        if new_head in self.snake[1:]:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.snake.pop()

# 清除終端螢幕
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 顯示遊戲畫面
def display_game(state):
    clear_screen()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == state.snake[0]:
                print(SNAKE_HEAD, end='')
            elif (x, y) in state.snake[1:]:
                print(SNAKE_BODY, end='')
            elif (x, y) == state.food:
                print(FOOD, end='')
            else:
                print(' ', end='')
        print()
    print(f'Score: {state.score}')

# 主遊戲迴圈
def main():
    state = GameState()

    while not state.game_over:
        display_game(state)
        time.sleep(0.1)

        # 處理玩家輸入
        direction = input("Enter direction (UP/DOWN/LEFT/RIGHT): ").upper()
        if direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            state.direction = direction

        state.move_snake()

    print("Game Over!")
    print(f"Score: {state.score}")

if __name__ == "__main__":
    main()

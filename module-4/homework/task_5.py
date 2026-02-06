import random

def create_board():
    board = list(range(1, 16)) + [0]
    random.shuffle(board)
    return [board[i:i+4] for i in range(0, 16, 4)]  

def print_board(board):
    print("\n" + "-" * 20)
    for row in board:
        print("|", end="")
        for cell in row:
            if cell == 0:
                print("    |", end="")
            else:
                print(f"{cell:3} |", end="")
        print("\n" + "-" * 20)

def find_empty(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i, j
    return -1, -1 

def is_solved(board):
    expected = list(range(1, 16)) + [0]
    flat = [board[i][j] for i in range(4) for j in range(4)]
    return flat == expected

def move(board, direction):
    i, j = find_empty(board)

    if direction == 'w' and i < 3:
        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        return True
    elif direction == 's' and i > 0:
        board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
        return True
    elif direction == 'a' and j < 3:
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        return True
    elif direction == 'd' and j > 0:
        board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
        return True
    return False 

def main():
    print("Добро пожаловать в Пятнашки!")
    print("Используйте: w — вверх, s — вниз, a — влево, d — вправо.")
    print("Цель: расположить числа по порядку, пустая клетка — внизу справа.")

    board = create_board()

    while not is_solved(board):
        print_board(board)
        cmd = input("Ваш ход (w/a/s/d): ").strip().lower()

        if cmd in ['w', 'a', 's', 'd']:
            if not move(board, cmd):
                print("Этот ход невозможен!")
        else:
            print("Неизвестная команда. Используйте w, a, s, d.")

    print_board(board)
    print("Поздравляю! Вы собрали Пятнашки!")

if __name__ == "__main__":
    main()
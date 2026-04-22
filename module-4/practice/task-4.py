def print_board(board):
    n = len(board)
    print("\n" + "-" * (4 * n + 1))
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell:2} |", end="")
        print("\n" + "-" * (4 * n + 1))

def is_valid(x, y, n, board):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def solve_knight_tour(board, x, y, move_count, n, moves):
    if move_count == n * n:
        return True
    
    for dx, dy in moves:
        next_x = x + dx
        next_y = y + dy

        if is_valid(next_x, next_y, n, board):
            board[next_x][next_y] = move_count
            if solve_knight_tour(board, next_x, next_y, move_count + 1, n, moves):
                return True
            
            board[next_x][next_y] = -1

    return False  
def main():
    n = 6 
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    board = [[-1 for _ in range(n)] for _ in range(n)]

    print(f"Введите начальные координаты коня (0..{n-1}):")
    try:
        start_x = int(input("x: "))
        start_y = int(input("y: "))
    except ValueError:
        print("Ошибка: введите целые числа!")
        return

    if not (0 <= start_x < n and 0 <= start_y < n):
        print(f"Координаты должны быть от 0 до {n-1}!")
        return
    
    board[start_x][start_y] = 0

    print(f"\nИщем маршрут для доски {n}×{n} из клетки ({start_x}, {start_y})...")
    if solve_knight_tour(board, start_x, start_y, 1, n, moves):
        print("Маршрут найден!")
        print_board(board)
    else:
        print("Маршрут не найден. Попробуйте другую начальную клетку.")

if __name__ == "__main__":
    main()
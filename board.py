board_list = list(range(1, 101))
free_cells = list(range(1, 101))


# Нумерация ячеек на доске
def generation_array(board):
    array = [list(board[:10])]
    for i in range(1, 10):
        array.append(board[10 * i:10 + 10 * i])
    return array


# Вывод игрового поля в консоли
def draw_board(board):
    array = generation_array(board)
    print("-" * 50)
    for i in range(10):
        for j in range(10):
            if str(array[i][j]) == "X":
                print("|", "\033[1;31m X \033[0m", end='')
            elif str(array[i][j]) == "O":
                print("|", "\033[32m O \033[0m", end='')
            else:
                print("|", str(array[i][j]).ljust(3), end='')
        print()
        print("-" * 50)
    print("\n" * 2)
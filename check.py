from board import generation_array


# Поиск проигрышных комбинаций
def check_entry(array):
    string = ""

    for j in array:
        string += str(j)

    if "X" * 5 in string:
        return "X"

    elif "O" * 5 in string:
        return "O"


# Проверка игрового поля
def check_board(board):
    array = generation_array(board)

    # По горизонтальным линиям
    for i in array:
        result = check_entry(i)
        if result:
            return result

    # По вертикальным линиям
    for i in range(10):
        dim = []
        for j in range(10):
            dim.append(array[j][i])
        result = check_entry(dim)
        if result:
            return result

    # По диагональным линиям
    diagonal = [[] for i in range(20 - 1)]
    rev_diagonal = [[] for i in range(len(diagonal))]
    min_rev_diagonal = -10 + 1

    for y in range(10):
        for x in range(10):
            diagonal[x + y].append(array[y][x])
            rev_diagonal[-min_rev_diagonal + x - y].append(array[y][x])

    for i in diagonal:
        result = check_entry(i)
        if result:
            return result

    for i in rev_diagonal:
        result = check_entry(i)
        if result:
            return result

    return False

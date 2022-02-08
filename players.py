from random import choice
from board import board_list, free_cells


# Выбор хода игрока
def player_turn(mark):
    valid = False

    while not valid:
        player_answer = input(f"Выберите номер ячейки для {mark}?")

        try:
            player_answer = int(player_answer)

        except:
            print("Некорректный ввод! Введите число, соответствующее номеру ячейки.")
            continue

        if 1 <= player_answer <= 100:

            if board_list[player_answer - 1] in free_cells:
                board_list[player_answer - 1] = mark
                free_cells.remove(player_answer)
                valid = True

            else:
                print("Данная ячейка уже занята!")

        else:
            print("Некорректный ввод! Введите число, соответствующее номеру ячейки.")


# Выбор ячейки для компьютера
def computer_turn(mark):
    computer_answer = choice(free_cells)
    board_list[computer_answer - 1] = mark
    free_cells.remove(computer_answer)

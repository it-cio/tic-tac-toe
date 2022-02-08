from board import board_list, draw_board
from check import check_board
from players import player_turn, computer_turn


# Главная функция для запуска игры
def main(board):
    counter = 0
    win = False
    player = "X"
    computer = "O"

    while not win:
        draw_board(board)

        if counter % 2 == 0:
            player_turn(player)
        else:
            computer_turn(computer)

        counter += 1

        if counter > 8:
            condition = check_board(board_list)

            if condition == "X":
                draw_board(board)
                print("\033[1;31m Компьютер выиграл! \033[0m")
                break
            elif condition == "O":
                draw_board(board)
                print("\033[1;31m Вы выиграли! \033[0m")
                break

        if counter == 101:
            print("Ничья!")
            break


if __name__ == '__main__':
    main(board_list)
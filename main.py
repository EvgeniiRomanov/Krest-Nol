# Консольная программа крестики-нолики 3*3
# Разработчик Романов Е.В.

from istruction import print_instruction

# Функция выводит игровое поле в процессе игры, не меняя никаких значений


def print_game_pole():

    print(" "*30, "-" * 17)
    print(" "*30, "-"*3, pole_global[0]," "*1, pole_global[1]," "*1, pole_global[2],"-"*3)
    print(" "*30, "-"*3, pole_global[3]," "*1, pole_global[4]," "*1, pole_global[5],"-"*3)
    print(" "*30, "-"*3, pole_global[6]," "*1, pole_global[7]," "*1, pole_global[8],"-"*3)
    print(" "*30, "-" * 17, "\n")

    return
# -----------------------------------------------------------------------------------------------------------------------
# Функция принимает номер игрока, проверяет введенную игроком ячейку на корректность,
# проверяет не занята ли уже ячейка и в случае успеха возвращает введенный номер ячейки


def number_correct(gamer_num, str_simbol):

    while True:
        try:
            print("Игрок №%d Введите номер ячейки, где будет поставлен %s:" %(gamer_num, str_simbol) +"\n")
            number_input = int(input("  "))
            if number_input not in range(1, 10):                                    # Если ввели не число
                print("Введен не корректный номер ячейки! Игрок №%d попробуйте снова!" %gamer_num +"\n")
            elif pole_global[number_input - 1] != number_input:
                print("Введеная ячейка уже занята! Игрок №%d попробуйте снова!" %gamer_num +"\n")
            else:                                                                   # Если ввели кореектное      # Вопрос как лучше через break
                break                                                                                           # или тут return number_input
        except ValueError:                                                          # Если ввели символ с клавиатуры
            print("Введен символ, а не номер ячейки. Игрок №%d попробуйте снова!" %gamer_num +"\n")

    return number_input
# ---------------------------------------------------------------------------------------------------------------------
# Функция получает на вход 'X' или '0' и проверяет комбинации выигрыша


def who_winner(winner):

    if (pole_global[0] == pole_global[1] == pole_global[2] == winner) or (         #Проверка горизонталей
        pole_global[3] == pole_global[4] == pole_global[5] == winner) or (
        pole_global[6] == pole_global[7] == pole_global[8] == winner) or (
        pole_global[0] == pole_global[3] == pole_global[6] == winner) or (         #Проверка вертикалей
        pole_global[1] == pole_global[4] == pole_global[7] == winner) or (
        pole_global[2] == pole_global[5] == pole_global[8] == winner) or (
        pole_global[0] == pole_global[4] == pole_global[8] == winner) or (         #Проверка диагоналей
        pole_global[2] == pole_global[4] == pole_global[6] == winner):

        return winner

# ----------------------------------------------------------------------------------------------------------------------


print_instruction()                 # Выводим инструкцию
pole_global = list(range(1, 10))    # Фомируем поле с ячейками 3 * 3
print_game_pole()                   # Выводим поле в начале игры

for index in range(len(pole_global)):
    if index % 2 == 0:                                  # Ход игрока №1 (0-2-4-6-8(для человека нечетные))
        gamer = 1
        first_gamer = number_correct(gamer, 'X')        # Проверка введенного значения на корректность и занятость ячейки
        pole_global[first_gamer-1] = 'X'                # Записываем значение в ячейку
        win1 = who_winner('X')                          # Проверяем условие выигрыша
        if index > 3:
            if win1 == 'X':
                print("* * * Поздравляем. Победил игрок №%d * * * \n" %gamer)
                print_game_pole()
                break
            elif index == 8:
                print_game_pole()
                print(" * * * У Вас ничья !!! * * *")
                break
            else:
                print_game_pole()
                print("Победитель не выявлен. Продолжаем игру \n \n")
        else:
            print_game_pole()
            print("Продолжаем игру!!!")

    else:                                                      # Ход игрока №2 (1-3-5-7(для человека четные))
        gamer = 2
        second_gamer = number_correct(gamer, 'O')              # Проверка корректности введенного значения и занятости ячейки
        pole_global[second_gamer - 1] = 'O'                    # Записываем значение в ячейку
        win2 = who_winner('O')                                 # Проверяем условие выигрыша
        if index > 3:
            if win2 == 'O':
                print("* * * Поздравляем. Победил игрок №%d * * * \n" %gamer)
                print_game_pole()
                break
            elif index == 8:
                print_game_pole()
                print(" * * * У Вас ничья !!! * * *")
                break
            else:
                print_game_pole()
                print("Победитель не выявлен. Продолжаем игру \n \n")
        else:
            print_game_pole()
            print("Продолжаем игру!!!")

print("Конец")

# подумать как передать в функцию вводимый игроком символ
# Консольная программа крестики-нолики
# Разработчик Романов Е.В.

#Функция выводит правила игры
def print_instruction():

    instruction = str("Инструкция: \n\nВ игре участвуют два игрока, поле для игры представляет собой квадрат размером 3 * 3 ячейки с номерам ячеек от 1 до 9.\n"
                       "Игрок который ходит первым (далее - игрок №1) выбирает номер ячейки и вводит её цифру, если ячейка не занята, на неё вместо цифры \n"
                       "выставляется символ 'Х'. Затем ходит второй игрок (далее - игрок №2), который выбирает номер ячейки и вводит её цифру, если ячейка \n"
                       "не занята, на неё вместо цифры выставляется символ 'O'. Игрок, который первым cоберёт комбинацияю из трех символов 'Х' или 'O', \n"
                       "расположенных по горизонтали, вертикали или диагонали, выигрывает. \n")

    print(instruction)

# Функция выводит игровое поле в начале игры
def print_start_pole():

    pole_ = list(range(1,10))
    print(" "*30, "-" * 17)
    print(" "*30, "-"*3, pole_[0]," "*1, pole_[1]," "*1, pole_[2],"-"*3)
    print(" "*30, "-"*3, pole_[3]," "*1, pole_[4]," "*1, pole_[5],"-"*3)
    print(" "*30, "-"*3, pole_[6]," "*1, pole_[7]," "*1, pole_[8],"-"*3)
    print(" "*30, "-" * 17, "\n")

# Функция выводит игровое поле в процессе игры, не меняя никаких значений
def print_game_pole():

    print(" "*30, "-" * 17)
    print(" "*30, "-"*3, pole_global[0]," "*1, pole_global[1]," "*1, pole_global[2],"-"*3)
    print(" "*30, "-"*3, pole_global[3]," "*1, pole_global[4]," "*1, pole_global[5],"-"*3)
    print(" "*30, "-"*3, pole_global[6]," "*1, pole_global[7]," "*1, pole_global[8],"-"*3)
    print(" "*30, "-" * 17, "\n")

#Функция проверяет введенное число
def number_correct():

    while True:
        try:
            number_input = int(input("Введите номер ячейки, где будет поставлен СИМВОЛ: "))
            if number_input not in range(1, 10):
                print("Введен не корректный номер ячейки! Попробуйте снова! \n")
            else:                                                                   # Вопрос как лучше через break
                break                                                               # или тут return number_input
        except ValueError:
            print("Введен символ, а не номер ячейки. Попробуйте снова! \n")

    return number_input

# Функция проверяет комбинации выигрыша
def who_winner(winner1):

    if winner1 == 'X':
        if (pole_global[0] == pole_global[1] == pole_global[2] == 'X') or (         #Проверка горизонталей
            pole_global[3] == pole_global[4] == pole_global[5] == 'X') or (
            pole_global[6] == pole_global[7] == pole_global[8] == 'X') or (
            pole_global[0] == pole_global[3] == pole_global[6] == 'X') or (         #Проверка вертикалей
            pole_global[1] == pole_global[4] == pole_global[7] == 'X') or (
            pole_global[2] == pole_global[5] == pole_global[8] == 'X') or (
            pole_global[0] == pole_global[4] == pole_global[8] == 'X') or (         #Проверка диагоналей
            pole_global[2] == pole_global[4] == pole_global[6] == 'X'):

            return winner1

    elif winner1 == 'O':
        if (pole_global[0] == pole_global[1] == pole_global[2] == 'O') or (         #Проверка горизонталей
            pole_global[3] == pole_global[4] == pole_global[5] == 'O') or (
            pole_global[6] == pole_global[7] == pole_global[8] == 'O') or (
            pole_global[0] == pole_global[3] == pole_global[6] == 'O') or (         #Проверка вертикалей
            pole_global[1] == pole_global[4] == pole_global[7] == 'O') or (
            pole_global[2] == pole_global[5] == pole_global[8] == 'O') or (
            pole_global[0] == pole_global[4] == pole_global[8] == 'O') or (         #Проверка диагоналей
            pole_global[2] == pole_global[4] == pole_global[6] == 'O'):

            return winner1

print_instruction()
pole_global = list(range(1,10))  #Глобальное поле
print_start_pole()

for index in range(len(pole_global)):
    if index % 2 == 0:                                  # Ход игрока №1 (нечетные ходы)
        first_gamer = number_correct()                  # Проверка введенного значения
        #Тут ввести функцию проверки ячейки на занятость (или отдельная или в исключения или как исключения)
        if pole_global[first_gamer-1] == first_gamer:   # Если ячейка не занята
            pole_global[first_gamer-1] = 'X'            # Записываем значение в ячейку
            win1 = who_winner('X')                      # Проверяем условие выигрыша
            if win1 == 'X':
                print("*** Поздравляем. Вы победили *** \n")
                print_game_pole()
                break
            else:
                print("Победитель не выявлен. Продолжаем игру \n \n")
                print_game_pole()
        else:
            print("Поле уже занято, введите другой номер поля \n \n")

    else:                                                      # Ход игрока №1 (нечетные ходы)
        second_gamer = number_correct()                        # Проверка введенного значения
        if pole_global[second_gamer - 1] == second_gamer:      # Если ячейка не занята
            pole_global[second_gamer - 1] = 'O'                # Записываем значение в ячейку
            win2 = who_winner('O')                             # Проверяем условие выигрыша
            if win2 == 'O':
                print("*** Поздравляем. Вы победили *** \n")
                print_game_pole()
                break
            else:
                print("Победитель не выявлен. Продолжаем игру \n \n")
                print_game_pole()
        else:
            print("Поле уже занято, введите другой номер поля \n \n")


# Сделать функцию проверки ячейки на занятость
# В комментах ввести номер игрока и чем он ходит

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

def print_game_pole():

#    pole_ = list(range(1,10))
    print(" "*30, "-" * 17)
    print(" "*30, "-"*3, pole_global[0]," "*1, pole_global[1]," "*1, pole_global[2],"-"*3)
    print(" "*30, "-"*3, pole_global[3]," "*1, pole_global[4]," "*1, pole_global[5],"-"*3)
    print(" "*30, "-"*3, pole_global[6]," "*1, pole_global[7]," "*1, pole_global[8],"-"*3)
    print(" "*30, "-" * 17, "\n")

# Функция проверяет комбинации выигрыша
def who_winner(a):

    if a == 'X':
        if (pole_global[0] == pole_global[1] == pole_global[2] == 'X') or (         #Проверка горизонталей
            pole_global[3] == pole_global[4] == pole_global[5] == 'X') or (
            pole_global[6] == pole_global[7] == pole_global[8] == 'X') or (
            pole_global[0] == pole_global[3] == pole_global[6] == 'X') or (         #Проверка вертикалей
            pole_global[1] == pole_global[4] == pole_global[7] == 'X') or (
            pole_global[2] == pole_global[5] == pole_global[8] == 'X') or (
            pole_global[0] == pole_global[4] == pole_global[8] == 'X') or (         #Проверка диагоналей
            pole_global[2] == pole_global[4] == pole_global[6] == 'X'):

            return a

    elif a == 'A':
        if (pole_global[0] == pole_global[1] == pole_global[2] == 'A') or (         #Проверка горизонталей
            pole_global[3] == pole_global[4] == pole_global[5] == 'A') or (
            pole_global[6] == pole_global[7] == pole_global[8] == 'A') or (
            pole_global[0] == pole_global[3] == pole_global[6] == 'A') or (         #Проверка вертикалей
            pole_global[1] == pole_global[4] == pole_global[7] == 'A') or (
            pole_global[2] == pole_global[5] == pole_global[8] == 'A') or (
            pole_global[0] == pole_global[4] == pole_global[8] == 'A') or (         #Проверка диагоналей
            pole_global[2] == pole_global[4] == pole_global[6] == 'A'):

            return a

pole_global = list(range(1,10))  #Глобальное поле
print(pole_global)
print_start_pole()

for index in range(len(pole_global)):
    if index % 2 == 0:  #ход игрока №1 (нечетные ходы)
        # !!! Тут надо как-то завернуть все это дело в функцию
        first_gamer = int(input("Игрок №1 введите номер поля, где будет поставлен Х: "))
        if 1 <= first_gamer <= 9:                           # Проверяем что число соответствует номеру ячейки
            if pole_global[first_gamer-1] == first_gamer:   # Если ячейка не занята
                pole_global[first_gamer-1] = 'X'            # Записываем значение в ячейку
                c = who_winner('X')                                            # Проверяем условие выигрыша
                if c == 'X':
                    print("Вы победили")
                    print(pole_global)
                    print_game_pole()
                    break
                else:
                    print("Продолжаем игру")
                    print(pole_global)
                    print_game_pole()
            else:
                print("Поле уже занято, введите другой номер поля")
        else:
            print("Вы ввели неверный номер поля, будьте внимательнее и повторите ход!")
    else:
        second_gamer = int(input("Игрок №2 введите номер поля, где будет поставлен O: "))
        if 1 <= second_gamer <= 9:  # Проверяем что число соответствует номеру ячейки
            if pole_global[second_gamer - 1] == second_gamer:
                pole_global[second_gamer - 1] = 'A'
                c1 = who_winner('A')  # Проверяем условие выигрыша
                if c1 == 'A':
                    print("Вы победили")
                    print(pole_global)
                    print_game_pole()
                    break
                else:
                    print("Продолжаем игру")
                    print(pole_global)
                    print_game_pole()
            else:
                print("Поле уже занято, введите другой номер поля")
        else:
            print("Вы ввели неверный номер поля, будьте внимательнее и повторите ход!")

#       Игра

#print_instruction()

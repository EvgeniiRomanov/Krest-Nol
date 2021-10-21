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

# Функция сравнения занятости введенного поля
# def print_game_pole(zanytost):
#
#     pole_zan_ = list(range(1, 10))
#     if pole_zan_[zanytost] == zanytost:
#
#
#     for value in range(len(pole_zan_)):
#         if zanytost > pole_zan_[value]
#     else:
#         print("Введенная ячейка" +str(zanytost) +"уже занята, будьте внимательнее выберите другую ячейку")
    # pole_ = list(range(1,10))
    # print(" "*30, "-" * 17)
    # print(" "*30, "-"*3, pole_[0]," "*1, pole_[1]," "*1, pole_[2],"-"*3)
    # print(" "*30, "-"*3, pole_[3]," "*1, pole_[4]," "*1, pole_[5],"-"*3)
    # print(" "*30, "-"*3, pole_[6]," "*1, pole_[7]," "*1, pole_[8],"-"*3)
    # print(" "*30, "-" * 17, "\n")


# # Функция проверки занятости поля
# # Функция проверки выигрыша
# #
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print('Hi', name)  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

#print_instruction()
#print_start_pole()

pole_global = list(range(1,10))  #Глобальное поле

print(pole_global)

for index in range(len(pole_global)):
    if index % 2 == 0:  #ход игрока №1 (нечетные ходы)
        first_gamer = int(input("Игрок №1 введите номер поля, где будет поставлен Х: "))
        if 1 <= first_gamer <= 9:                   # Проверяем что число соответствует номеру ячейки
            if pole_global[first_gamer-1] == first_gamer:
                pole_global[first_gamer-1] = 'X'
                print(pole_global)
                #print("Установили", pole_global[first_gamer-1], "в ячейку", first_gamer-1, "\n", pole_global)
            else:
                print("Поле уже занято, введите другой номер поля")
        else:
            print("Вы ввели неверный номер поля, будьте внимательнее и повторите ход!")
    else:
        second_gamer = int(input("Игрок №2 введите номер поля, где будет поставлен O: "))
        if 1 <= second_gamer <= 9:  # Проверяем что число соответствует номеру ячейки
            if pole_global[second_gamer - 1] == second_gamer:
                pole_global[second_gamer - 1] = 'O'
                print(pole_global)
                # print("Установили", pole_global[second_gamer-1], "в ячейку", second_gamer-1, "\n", pole_global)
            else:
                print("Поле уже занято, введите другой номер поля")
        else:
            print("Вы ввели неверный номер поля, будьте внимательнее и повторите ход!")


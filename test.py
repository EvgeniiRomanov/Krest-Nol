# #Функция проверяет введенное число
# def number_correct():
#
#     while True:
#         try:
#             number_input = int(input("Введите номер ячейки, где будет поставлен СИМВОЛ: "))
#             if number_input not in range(1, 10):
#                 print("Введен не корректный номер ячейки! Попробуйте снова!")
#             else:                                                                   # Вопрос как лучше через break
#                 break                                                               # или тут return number_input
#         except ValueError:
#             print("Введен символ, а не номер ячейки. Попробуйте снова!")
#     return number_input
#
# a = number_correct()
# print(a)
#     # try:
#     #     number_input = int(number_input)
#     # if number_input in range(1, 10):
#     #     return number_input
#     # elif 9 < number_input < 0:
#     #     print("Введено не корректное числовое значение ячейки! Попробуйте снова!")
#     #     return
#     # else:
#     #     print("Введено не числовое значение или ничего не введено! Попробуйте снова!")
pole_global = list(range(1,10))  # Фомируем поле с ячейками 3 * 3
            # Выводим поле в начале игры

print(pole_global)))
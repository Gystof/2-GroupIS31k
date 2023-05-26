# Напишите две функции S(r) и l(r), принимающие в качестве
# аргумента радиус окружности и возвращающие площадь круга и длину этой
# окружности соответственно. Затем напишите функцию krug(), которая спрашивает у
# пользователя радиус окружности, а затем при помощи функций S(r) и l(r) выводит
# на экран площадь круга и длину окружности, разделённые пробелом.

# import math
#
#
# def S(r):
#     return math.pi * r ** 2
#
#
# def l(r):
#     return 2 * math.pi * r
#
#
# def krug():
#     radius = float(input("Введите радиус окружности: "))
#     area = S(radius)
#     length = l(radius)
#     print("Площадь круга:", area, '\n', "Длина окружности:", length)
#
#
# krug()

# Составить программу, согласно полученному варианту задания.
# Ввод данных сопровождать соответствующими запросами, а вывод -
# наименованиями выводимых переменных. Напишите функцию, которая принимает в качестве аргумента список,
# состоящий из номера дня недели и языка (русский или английский), а
# возвращает его название. В программе обеспечить ввод списка с клавиатуры


# def getDayName(day_list):
#
#     day, language = day_list[0], day_list[1]
#
#     if language.lower() == 'русский':
#         if day == 1:
#             return 'Понедельник'
#         elif day == 2:
#             return 'Вторник'
#         elif day == 3:
#             return 'Среда'
#         elif day == 4:
#             return 'Четверг'
#         elif day == 5:
#             return 'Пятница'
#         elif day == 6:
#             return 'Суббота'
#         elif day == 7:
#             return 'Воскресенье'
#         else:
#             return 'Неверный номер дня'
#     elif language.lower() == 'английский':
#         if day == 1:
#             return 'Monday'
#         elif day == 2:
#             return 'Tuesday'
#         elif day == 3:
#             return 'Wednesday'
#         elif day == 4:
#             return 'Thursday'
#         elif day == 5:
#             return 'Friday'
#         elif day == 6:
#             return 'Saturday'
#         elif day == 7:
#             return 'Sunday'
#         else:
#             return 'Invalid day number'
#     else:
#         return 'Неверный язык'
#
#
# day, language = int(input("Введите номер дня недели (1-7): ")), input("Введите язык (русский или английский): ")
#
# dayList = [day, language]
#
# dayName = getDayName(dayList)
# print("Название дня недели:", dayName)

def processLists(numbers, a, b, c):

    filteredNumbers = []
    sumOfOthers = 0

    for number in numbers:
        if number > a and number < b and number % c == 0:
            filteredNumbers.append(number)
        else:
            sumOfOthers += number

    print("Элементы, удовлетворяющие условиям:", filteredNumbers, '\n', "Сумма остальных элементов:", sumOfOthers)


numbers = [5, 10, 15, 20, 25, 30, 35, 40]

a, b, c = 10, 30, 5

processLists(numbers, a, b, c)

# Задание 1. Создать программу, используя цикл с условием (while), в которой
# пользователь вводит любые числа одно за другим на отдельных строках до тех пор,
# пока не введёт ноль. Программа должна выводить числа, обратные введенным числам.

# number = 1
#
# while number != 0:
#     number = int(input('Введите число: '))
#     if number != 0:
#         print(1 / number)

# Задание 2. Создать программу, используя цикл с условием (while), согласно
# заданию, указанному в таблице. Ввод данных сопровождать соответствующими
# запросами, а вывод - наименованиями выводимых переменных.

# Вычислить сумму кубов нечетных чисел от 7 до 37.

number, sumOfCubes = 7, 0

while number <= 37:
    if number % 2 != 0:
        sumOfCubes += number ** 3
    number += 1

print("Сумма кубов нечетных чисел от 7 до 37 равна:", sumOfCubes)
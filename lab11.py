# Составить программу, которая считывает сначала количество
# оценок, потом по очереди сами эти оценки, затем выводит их же в том же порядке
# (используем список). Найдите среднюю оценку за урок.


# numGrades = int(input("Введите количество оценок: "))
#
# grades = []
# for i in range(numGrades):
#     grade = float(input("Введите оценку: "))
#     grades.append(grade)
#
# averageGrade = sum(grades) / numGrades
#
# print("Оценки:", grade, '\n', "Средняя оценка:", averageGrade)

# Составить программу, согласно полученному варианту задания.
# Ввод данных сопровождать соответствующими запросами, а вывод - наименованиями выводимых переменных.

# Информация о температуре воздуха за март задана в виде списка.
# Определить сколько раз температура опускалась ниже 0° С.


# temperatures = list(map(int, input("Введите температуры воздуха за март через пробел: ").split()))
#
# countZero = 0
# for temp in temperatures:
#     if temp < 0:
#         countZero += 1
#
# print("Количество раз, когда температура опускалась ниже 0°C:", countZero)

# Составить программу, согласно полученному варианту задания.
# Ввод данных сопровождать соответствующими запросами, а вывод - наименованиями выводимых переменных

# Дан список вещественных чисел, содержащий 12 элементов, записать в
# этот же массив сначала все отрицательные числа, а затем все
# положительные, сохраняя порядок их следования.

numbers = list(map(float, input("Введите список вещественных чисел через пробел: ").split()))

negativeNumbers = []
positiveNumbers = []

for num in numbers:
    if num < 0:
        negativeNumbers.append(num)
    else:
        positiveNumbers.append(num)

numbers = negativeNumbers + positiveNumbers

print("Обновленный список чисел:", numbers)

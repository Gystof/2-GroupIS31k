# Задание 1. Напишите программу, используя цикл с переменной (for), которая
# считывает одно число k, после чего для каждого из чисел от 0 до k (включительно)
# выводит фразу: «Корень числа [такого-то] равен [тому-то], а куб равен [тому-то]»

# k = int(input("Введите число k: "))
# for i in range(k+1):
#     print(f"Корень числа {i} равен {i**0.5}, а куб равен {i**3}")

# Задание 2. Создать программу, используя цикл с переменной (for), согласно
# заданию, указанному в таблице. Ввод данных сопровождать соответствующими
# запросами, а вывод - наименованиями выводимых переменных.

# Вычислить сумму квадратов первых n-четных чисел натурального ряда ( n= 30 )

n, sumOfSquares = 30, 0

for i in range(2, n * 2 + 1, 2):
    sumOfSquares += i ** 2
print(f"n = {n}\nСумма квадратов = {sumOfSquares}")


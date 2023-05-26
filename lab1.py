# 1 Задание

print('Привет,Python!')
print('Приятно познакомиться.')

# 2 Задание


inputFilm = input('Введите название фильма: ')
inputName = input('Введите название кинотеатра: ')
inputTime = input('Введите время бронирование: ')

print(f'«Билет на {inputFilm} в {inputName} на {inputTime} забронирован.»')
#
# 3 Задание

a = int(input('Введите целое число: '))
b = int(input('Введите целое число: '))
c = int(input('Введите целое число: '))

print('Сумма:', a + b + c)
print('Произведение:', (a * b) * c)
print('Сумма:', (a + b + c) / 3)

# 4 Задание

from random import randint

a = randint(100, 999)
print(str(a)[0] + ', ', str(a)[1] + ', ', str(a)[2] + '.')

# 5 Задание

r = int(input('Введите стоимость пирожка (рублей и копеек): '))
k = int(input())
p = int(input('Сколько пирожков: '))
r1 = 0
k1 = 0
for i in range(p):
    r1 += r
    k1 += k
    r1 += k1 // 100
    k1 = k1 % 100
print('К оплате: ', r1, ' руб. ', k1, ' коп.')




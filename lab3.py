
# Задание 1. Вводятся два целых числа. Проверить делится ли первое на второе.
# Если первое число нацело делится на второе, то вывести сообщение об этом, иначе
# вывести сообщение о том, что первое число не делится на второе.

a, b = int(input('Введите первое число: ')), int(input('Введите второе число: '))

if a % b == 0:
    print(f'{a} делится на {b}')
else:
    print(f'{a} не делится на {b}')

# Задание 2. Создать программу, используя оператор условия, согласно заданию,
# указанному в таблице. Ввод данных сопровождать соответствующими запросами, а
# вывод - наименованиями выводимых переменных.

# Написать программу – модель анализа пожарного датчика в
# помещении, которая выводит сообщение «Пожароопасная ситуация»,
# если температура в комнате превысила 60ºС.

temperature = float(input('Введите температуру в комнате: '))

if temperature > 60:
    print(f'Пожароопасная ситуация температура {temperature}')
else:
    print(f'Погода {temperature} оптимальна температура')

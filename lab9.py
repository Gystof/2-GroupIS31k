# Напишите программу, которая считывает подряд две строки, после
# чего выводит «ВЕРНО», если последний символ первой строки совпадает с первым
# символом второй, и «НЕВЕРНО» в противном случае.
# Ввод данных сопровождать соответствующими запросами, а вывод - наименованиями выводимых данных

#
# a, b = input("Введите первую строку: "), input("Введите вторую строку: ")
#
# if a[-1] == b[0]:
#     print("ВЕРНО")
# else:
#     print("НЕВЕРНО")

# Создать программу, согласно заданию, указанному в таблице. Ввод
# данных сопровождать соответствующими запросами, а вывод - наименованиями
# выводимых данных


fileName = input("Введите имя файла: ")
fileExtension = fileName.split(".")[-1]

print("Расширение файла:", fileExtension)


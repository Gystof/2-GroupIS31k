# Дана строка, содержащая номера слов через пробел, затем строка,
# содержащая сами слова, записанные через пробел. Напишите программу, которая
# составляет новое предложение по номерам слов из исходной строки. Предложение должно начинаться с большой буквы.

wordIndexes, words = input("Введите номера слов через пробел: "), input("Введите слова через пробел: ")

wordIndexesList = wordIndexes.split()
wordsList = words.split()

newSentence = ""
for index in wordIndexesList:
    word = wordsList[int(index) - 1]
    newSentence += word + " "

newSentence = newSentence.strip()
newSentence = newSentence[0].upper() + newSentence[1:]

print("Новое предложение:", newSentence)

# Составить программу, согласно полученному варианту задания.
# Ввод данных сопровождать соответствующими запросами, а вывод -
# наименованиями выводимых переменных.

# Дана строка: слова, разделённые пробелами. Найдите длину самого
# длинного из введённых слов


sentence = input("Введите строку: ")

words = sentence.split()


maxLength = 0
for word in words:
    length = len(word)
    if length > maxLength:
        maxLength = length

print("Длина самого длинного слова:", maxLength)




# Создать программу, если дана строка из слов, разделенных
# пробелами. Переставить слова в обратном порядке и вывести результат – новую строку.
# Ввод данных сопровождать соответствующими запросами, а вывод - наименованиями выводимых данных.

def reverseWords(sentence):

    words = sentence.split()
    reversedWords = list(reversed(words))
    reversedSentence = ' '.join(reversedWords)

    return reversedSentence


inputSentence = input("Введите строку из слов, разделенных пробелами: ")
reversedSentence = reverseWords(inputSentence)

print("Новая строка:", reversedSentence)


# Создать программу, согласно заданию, указанному в таблице. Ввод
# данных сопровождать соответствующими запросами, а вывод - наименованиями выводимых данных.

# В строке между словами вставить вместо пробела запятую и пробел

def replaces():

    inputData = input("Введите данные: ")
    replacedData = inputData.replace(' ', ', ')

    print("Результат:")
    print(replacedData)


replaces()

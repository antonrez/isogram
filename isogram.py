"""
Написать функцию, которая определяет, является ли слово изограммой.
Изограммой является слово, в котором все буквы уникальны.
Примеры изограмм:
звукосниматель
разгильдяйство
lumberjacks
background

Для обхода строки можно использовать цикл
for c in my_str:
    #your code here
"""

user_word = input("Enter word: ")


def isogram(word):
    for s in word:
        if word.count(s) > 1:
            print("Word is not isogram")
            break
    else:
        print("Word is isogram")


def count_letter(word):
    word = word.lower()
    for s in word:
        if word.count(s) == 1:
            print(s, end="")
        else:
            print(s.upper(), end="")


isogram(user_word)
count_letter(user_word)

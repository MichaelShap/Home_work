# Напишите программу, которая принимает список строк
# и возвращает новый список, содержащий длины строк, возведенные в квадрат,
# с использованием функции `map`.
#
# Пример ввода:
# ["apple", "banana", "cherry"]
#
# Ожидаемый вывод:
# [25, 36, 36]

def square_lenght(words):
    words = words.split()
    for i in words:
        dlina = len(i)
        return dlina ** 2

fruti_list = ["apple", "banana", "cherry"]
map_list = list(map(square_lenght, fruti_list))

print(map_list)
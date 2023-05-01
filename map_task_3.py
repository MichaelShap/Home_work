# Задача 3
# Напишите программу, которая принимает список чисел в виде строк и
# возвращает новый список, содержащий только четные числа, возведенные в
# квадрат, с использованием функции `map`.
#
# Пример ввода:
#
# ["1", "2", "3", "4", "5"]
#
# Ожидаемый вывод:
# [4, 16]

def chet_nechet(list):
    if list % 2 == 0:
        return list ** 2

num_list = ["1", "2", "3", "4", "5"]
num_list = list(map(int, num_list))

map_list = list(map(chet_nechet, num_list))

while None in map_list:
    map_list.remove(None)

print(map_list)
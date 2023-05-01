# Задача 1
# Напишите программу, которая принимает список целых чисел и возвращает
# новый список, содержащий только нечетные числа, умноженные на 2,
# с использованием функции `map`.
#
# Пример ввода:
# [1, 2, 3, 4, 5]
#
# Ожидаемый вывод:
# [2, 6, 10]

def chet_nechet(list):
    if list % 2 != 0:
        return list * 2

num_list = [1, 2, 3, 4, 5]
map_list = list(map(chet_nechet, num_list))

while None in map_list:
    map_list.remove(None)

print(map_list)


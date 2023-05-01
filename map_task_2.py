# Задача 2
# Напишите программу, которая принимает список строк
# и возвращает новый список, содержащий только заглавные буквы в каждой строке,
# с использованием функции `map`.
#
# Пример ввода:
# ["Apple", "banana", "Cherry", "date"]
#
# Ожидаемый вывод:
# ["A", "C"]

def big_letters(letters):
    for i in letters:
        if i.isupper() == True:
            return i

fruti_list = input('vvedite spisok: ')
map_list = list(map(big_letters, fruti_list))

while None in map_list:
    map_list.remove(None)

print(map_list)

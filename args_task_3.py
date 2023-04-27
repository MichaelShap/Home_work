# Задача 3
# Напишите функцию `print_user_data`, которая принимает произвольное число
# именованных аргументов **kwargs,
# представляющих информацию о пользователе (имя, возраст, город и т.д.), и
# выводит эту информацию в отформатированном виде.
#
# Пример использования:
# print_user_data(name="John", age=30, city="New York", occupation="Programmer")
#
# Вывод:
# Name: John
# Age: 30
# City: New York
# Occupation: Programmer

def print_user_data(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

print_user_data(Name="John", Age=30, City="New York", Occupation="Programmer")
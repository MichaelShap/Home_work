# Задача 2
# Напишите декоратор, который добавляет к результату функции префикс и суффикс.
# Префикс и суффикс должны задаваться при вызове декоратора.

# Пример:
# @add_prefix_suffix("Result: ", "!")
# def my_func():
#     return "Hello, world"
#
# result = my_func()
# print(result) # Result: Hello, world!

def add_prefix_suffix(func):
    def wrapper(data):
        new_list = []
        lists = [data]
        new_list.append('Result: ' + data + "!")

        print(new_list)

    return wrapper

@add_prefix_suffix
def my_func():
    return my_func
my_func = add_prefix_suffix(my_func)
my_func("Hello, world")

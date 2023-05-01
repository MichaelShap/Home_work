# Задача 1
# Напишите декоратор, который проверяет, что результат функции является
# числом, и возвращает его. Если результат не является числом, декоратор
# должен вернуть None.
#
# Пример:
# @check_type
# def my_func():
#     return 42
#
# result = my_func()
# print(result) # 42
#
# @check_type
# def my_func():
#     return "Hello, world!"
#
#  result = my_func()
# print(result) # None.


def check_type(func):
    def wrapper(data):
        if type(data) == int:
            print(data)
        else:
            print(None)

    return  wrapper

# V1
@check_type
def my_func():
    return my_func

my_func = check_type(my_func)
my_func(42)

# V2
@check_type
def my_func2():
    return my_func2

my_func2 = check_type(my_func2)
my_func2("Hello, world!")


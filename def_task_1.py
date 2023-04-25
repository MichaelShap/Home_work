# Задача 1
# Напишите функцию с именем add_excitement, которая берет список строк
# и добавляет восклицательный знак (!) в конец каждой строки в списке.
# Программа должна изменить исходный список и ничего не возвращать.
# 2. (а)
# (b) Напишите ту же функцию, за исключением того,
# что она не должна изменять исходный список и вместо этого должна возвращать новый список.

# VAR a
initial_list = ['python', 'is', 'number', 'one']
def add_excitement(string):
    return string + '123'
initial_list = list(map(add_excitement, initial_list))


# VAR b
initial_list = ['python', 'is', 'number', 'one']
def add_excitement(string):
    return string + '!'
converted_list = list(map(add_excitement, initial_list))
print(converted_list)
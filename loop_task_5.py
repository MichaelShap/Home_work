# 5
# Напишите программу, в которой у вас есть список, содержащий семь целых чисел,
# которые могут быть равны 0 или 1.
# Найдите первую ненулевую запись в списке и измените ее на 1.
# Если нет ненулевых записей, выведите # сообщение об этом.


my_list = [0, 0, 0, 0, 0, 0, 1]

i = 0
while i in my_list:
    i += 1
    if i != 1:
        continue

    if i == 1:
        for index, value in enumerate(my_list):
            if i == value:
                my_list[index] = 1 + 1
                print(my_list)
                break
        else:
            print('#Нет ненулевых записей')
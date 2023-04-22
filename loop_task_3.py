# 3
# Напишите программу для игры в следующую игру.
# Существует список нескольких названий стран и программа случайным образом выбирает один.
# Затем игрок должен угадывать буквы в слове по одной.
# Перед каждым угадыванием отображается название страны
# с заполненными правильно угаданными буквами и остальные буквы представлены тире.
# Например, если страна Канада и игрок правильно угадал a, d и n,
# программа отобразит -ana-da.
# Программа следует продолжать до тех пор, пока игрок либо не угадает все буквы слова,
# либо не наберет пять букв. неправильный.


import random
cities = ['BISHKEK', 'OSH', 'BATKEN', 'TALAS', 'NARYN']
city = random.choice(cities)

city_list = list("_" * len(city))

i = 0
while "_" in city_list:
    letter = input("Введите букву: ")

    if not letter or len(letter) > 1:
        print("Ошибка ввода: Введите одну букву: ")
        continue

    if letter.upper() in city:
        for index, value in enumerate(city):
            if letter.upper() == value:
                city_list[index] = letter.upper()
        print("".join(city_list))

    else:
        i += 1
        if i == 5:
            print('Вы проиграли, все доступные попытки потрачены')
            print("Это был город", city)
            break
        print("Такой буквы в слове нет.")


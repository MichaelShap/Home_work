# sfsddf
# Напишите программу, которая использует цикл while (а не цикл for)
# для чтения и вывода каждого символа строки один за другим на отдельных строках.

number = input('vvedite num: ')
while True:
    if number.isalnum():
        for i in number:
            print(i)
        break
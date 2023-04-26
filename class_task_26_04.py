# Ќапишите программу, котора€ запрашивает у пользовател€ число,
# а затем выводит синус, косинус и тангенс этого числа.

import math
def calculatuions(x):
    return "cos = {0}".format(math.cos(x)), \
        "sin = {0}".format(math.sin(x)), \
        "tan = {0}".format(math.tan(x))

print(calculatuions(int(input('Введите число: '))))
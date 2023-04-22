# 2
# Напишите программу, которая просит пользователя ввести пароль.
# Если пользователь вводит правильный пароль, программа должна сообщить им,
# что они вошли в систему.
# В противном случае следует попросить их повторно ввести пароль.
# Пользователю дается только 5 попыток на ввод пароля,
# после чего программа должна сообщить им, что они удалены из системы.

password = str(input('Enter the password: '))
correct_password = 'v'
i = 0
while password != correct_password:
    i += 1
    if i < 5:
        password = str(input('The passwor is wrong. Enter the password: '))
        continue

    if i == 5:
        print('Your account delited')
        break

else:
    print('Access granted!')

# Компьютер загадывает случайное число от 1 до 100.
# Пользователю предлагается его угадать.
# Если пользователь угадал, программа сообщает о победе.
# Если пользователь ввел неверно число, программа дает ему подсказку: введенное число больше или меньше загаданного.
import random

number = random.randint(1, 100)
user_number = None
print(number)

while user_number != number:
    user_number = int(input('Введите загаданное число: '))
    if user_number > number:
        print('Введенный вариант больше загаданного.')
    elif user_number < number:
        print('Введенный вариант меньше загаданного.')
    else:
        print('Ура, вы угадали')

# Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых.
# И просите ввести заново. Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.


while True:
    number = int(input('Введите число: '))
    if 0 < number < 10:
        print(number ** 2)
        break
    else:
        print('Число должно быть меньше 0 и больше 10')


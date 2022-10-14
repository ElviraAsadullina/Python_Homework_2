def check_for_input_error_int():
    while True:
        try:
            a = int(input('Введите любое натуральное число: '))
        except ValueError:
            print('Ошибка - необходимо ввести натуральное число!')
            continue
        if  a < 1:
            print('Ошибка - число должно быть положительным!')
            continue
        break
    return a
def check_for_input_error_position(a):
    while True:
        try:
            b = int(input(f'Введите позицию элемента списка в диапазоне от {0} до введенного числа: '))
        except ValueError:
            print('Ошибка - необходимо ввести натуральное число!')
            continue
        if  b < 0 or b > a - 1:
            print('Ошибка - число должно быть в пределах указанного диапазона!')
            continue
        break
    return b
def get_sum_of_specified_elements(collection, a):
    import random
    count = random.randint(1, a)
    print(count)
    i = 0
    sum = 0
    while i < count:
        position = check_for_input_error_position(a)
        # position = int(input(f'Введите позицию элемента списка в диапазоне от {0} до {a - 1}: '))
        sum += collection[position]
        i += 1
    return sum
N = check_for_input_error_int()
from random import sample
roll = sample(range(-N, N + 1), N)
print(roll)
print(f'Сумма элементов на указанных позициях = {get_sum_of_specified_elements(roll, N)}')
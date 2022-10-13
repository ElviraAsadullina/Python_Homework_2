def check_for_input_error():
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
def get_roll_of_factorial(a):
    roll = []
    factorial = 1
    for i in range(1, a + 1):
        factorial *= i
        roll += [factorial]
    return roll
N = check_for_input_error()
# catalogue = get_roll_of_factorial(N)
print(f'Набор произведений чисел от 1 до {N}:  {get_roll_of_factorial(N)}')
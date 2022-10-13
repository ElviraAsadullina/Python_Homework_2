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
def list_from_int(a):
    listed_a = []
    stringed_a = str(a)
    for i in stringed_a:
        listed_a.append(int(i))
    return listed_a
def get_factorial(a):
    factorial = 1
    for i in a:
        factorial *= i
    return factorial
N = check_for_input_error()
print(f'Факториал введенного числа = {get_factorial(list_from_int(N))}')
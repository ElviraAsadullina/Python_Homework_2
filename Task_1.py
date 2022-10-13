def check_for_input_error():
    while True:
        try:
            a = float(input('Введите любое вещественное число: '))
        except ValueError:
            print('Ошибка - введено не числовое значение!')
            continue
        return a
def list_from_float(a):
    listed_a = []
    stringed_a = str(a)
    for i in stringed_a:
        if i == '.' or i == '0' or i == '-':
            continue
        else:
            listed_a.append(int(i))
    return listed_a
def get_sum(list_a):
    sum = 0
    for i in list_a:
        sum += i
    return sum
number = check_for_input_error()
print(f'Сумма элементов введенного числа = {get_sum(list_from_float(number))}')
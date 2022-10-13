def check_for_input_error(a):
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
    for i in listed_number:
        sum += i
    return sum
number = None
number = check_for_input_error(number)
listed_number = list_from_float(number)
print(f'Сумма элементов введенного числа = {get_sum(listed_number)}')
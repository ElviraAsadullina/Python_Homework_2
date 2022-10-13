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
def get_dictionary_in_order(a):
    dictionary = {}
    for i in range(1, a + 1):
        dictionary[i] = (1 + 1 / i) ** i
    return dictionary
def get_sum_of_dictionary_elements(dictionary):
    sum = 0
    for v in dictionary.values():
        sum += v
    return sum
n = check_for_input_error_int()
# roll = get_dictionary_in_order(n)
# get_sum_of_dictionary_elements(roll)
print(f'Сумма {n} элементов в заданной последовательности = {get_sum_of_dictionary_elements(get_dictionary_in_order(n)):.2f}')

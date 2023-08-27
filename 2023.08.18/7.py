def int_base(number: str, this_num_sys: int, num_sys_con: int) -> str | None:

    number = number.lower()
    num_sys_36 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num_sys_0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    dict_num = dict([*zip(num_sys_36, num_sys_0)])
    dict_num_two = dict([*zip(num_sys_0, num_sys_36)])
    # Проверка на коректности ввода данных с системой исчисления;
    for n in number:
        if dict_num[n] > this_num_sys:
            return print(None)
    
    # Преобразование числа n-го исчисления в десятичный;
    gen_work_num = (dict_num[number[i]] * (this_num_sys ** (len(number) - 1 - i)) for i in range(len(number)))
    ten_num = sum(gen_work_num) # - десятичное число;
    
    # Создание массива данных по разряду числа n-го исчисления;
    discharge = 0 # - разряжы результирующего данного;
    work_div = ten_num # - рабочая сумма для определения разрядов резултирующего данного;
    while True:
        work_div = work_div // num_sys_con
        discharge += 1
        if work_div == 0:
            break
    result_number_key = []
    for n in range(discharge):
        result_number_key.append(int(0))
    
    # Создание ключей числа n-го исчисления;
    for ch in range(ten_num):
        result_number_key[0] += 1
        i = 1
        while i < len(result_number_key):
            if result_number_key[i-1] == num_sys_con:
                result_number_key[i-1] = 0
                result_number_key[i] += 1
            i += 1

    # Результат;
    return ''.join((dict_num_two[key] for key in result_number_key[::-1]))

# >>> int_base('ff00', 16, 2)
# '1111111100000000'
# >>> int_base('1101010', 2, 30)
# '3g'

# >>> int_base('12345', 3, 30)
# None

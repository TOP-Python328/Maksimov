num_sys_36 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# ИСПОЛЬЗОВАТЬ: создание списка с распаковкой в его элементы возвращаемого значения функции zip() избыточно — функция dict() работает с любыми итерируемыми объектами, включая объекты генераторы, возвращаемые zip()
dict_num = dict(zip(num_sys_36, range(0, 36)))
dict_num_two = dict(enumerate(num_sys_36))

def int_base(number: str, this_num_sys: int, num_sys_con: int) -> str | None:
    """Функция преобразовывает число из произвольной системы счисления в число десятичной системы исчисления"""
    number = number.lower()

    # Проверка на коректности ввода данных с системой исчисления;
    for n in number:
        if dict_num[n] > this_num_sys:
            return None
    
    # Преобразование числа n-го исчисления в десятичный;
    len_num = len(number)
    # ИСПОЛЬЗОВАТЬ: встроенную функцию enumerate()
    # десятичное число;
    ten_num = sum(
        dict_num[num] * this_num_sys**(len_num-i-1)
        for i, num in enumerate(number)
    )
    
    # Создание массива данных по разряду числа n-го исчисления;
    rank = 0
    work_div = ten_num
    result_number_key = []
    while True:
        work_div = work_div // num_sys_con
        result_number_key.append(int(0))
        rank += 1
        if work_div == 0:
            break
    # УДАЛИТЬ: переменная не используется
    i = 1
    return result_funk(result_number_key, ten_num, num_sys_con)


# КОММЕНТАРИЙ: в данной задаче было бы оптимально написать три функции: первая преобразовывает из произвольной системы в десятичную, вторая преобразовывает из десятичной в произвольную — требуемая функция int_base() тогда станет третьей, и может использовать первые две функции, предварительно выполнив проверку на корректность переданного числа; каждая из трёх функций тогда была бы самостоятельно полезной и могла бы использоваться автономно
def result_funk(res_num: list[int], ten_num: int, num_sys_con: int):
    """Функция преобразует десятичное число в произвольную систему счисления число"""
    for ch in range(ten_num):
        res_num[0] += 1
        i = 1
        while i < len(res_num):
            if res_num[i-1] == num_sys_con:
                res_num[i-1] = 0
                res_num[i] += 1
            i += 1
    # Результат;
    return ''.join((dict_num_two[key] for key in res_num[::-1]))


# >>> int_base('ff00', 16, 2)
# '1111111100000000'
# >>> int_base('1101010', 2, 30)
# '3g'
# >>> print(int_base('12345', 3, 30))
# None


# ИТОГ: удовлетворительно — 4/8

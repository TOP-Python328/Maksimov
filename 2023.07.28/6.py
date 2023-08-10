binary_number = input('введите двоичное число: ')
bin_plenty = {'b', '1', '0'}
x = list(binary_number)

gen_binary = [({str(n)} < bin_plenty) for n in x]
while True:
    for k in range(len(x)):
        if gen_binary[k - 1] == False:
            print(f'\n{"нет"}\n')
            break

    if (str(x[0]) == '0' and str(x[1]) == 'b') or (str(x[0]) == 'b' and str(x[1]) != 'b') or (str(x[0]) != '1' and str(x[1]) == 'b') or (str(x[0]) != 'b' and str(x[1]) != 'b'):
        print(f'\n{"да"}\n')
    else:
        print(f'\n{"нет"}\n')
    break

# C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.07.28>python -i 6.py
# введите двоичное число: 0101

# да

# >>> ^Z


# C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.07.28>python -i 6.py
# введите двоичное число: b11

# да

# >>> ^Z


# C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.07.28>python -i 6.py
# введите двоичное число: 0b11001

# да

# >>> ^Z


# C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.07.28>python -i 6.py
# введите двоичное число: 1b0101

# нет

# >>>
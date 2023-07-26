simvol_one = int(input('введите начальное число Фибоначчи: '))
print(simvol_one)

simvol_two = int(input('введите количество чисел Фибоначчи: '))
array_number = [simvol_one, simvol_one]
array_str = ''
n = 0
while n < (simvol_two - 2):
    num = array_number[-1] + array_number[-2]
    array_number += [num]
    n += 1
for t in array_number:
    array_str += str(t) + ' '
    
print(array_str)

#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.33. ДЗ (Циклы, range(), генераторные выражения)>python -i 8.py
#введите начальное число Фибоначчи: 1
#1
#введите количество чисел Фибоначчи: 17
#1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
#>>>
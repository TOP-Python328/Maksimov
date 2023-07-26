
array_0 = ''
while True:
    std = input('введите число: ')
    if float(std) % 7 == 0:
        array_0 = std + ' ' + array_0
    else:
        print(array_0)
        break
        
#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.33. ДЗ (Циклы, range(), генераторные выражения)>python -i 1.py
#введите число: 7
#введите число: 14
#введите число: 21
#введите число: 15
#21 14 7
#>>>
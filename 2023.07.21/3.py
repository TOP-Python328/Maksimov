
n = int(input('введите число: '))
x = 1
sum_n = 0
while x <= n:
    if n % x == 0:
        sum_n += x
    x += 1
print(sum_n)

#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.33. ДЗ (Циклы, range(), генераторные выражения)>python -i 3.py
#введите число: 50
#93
#>>>
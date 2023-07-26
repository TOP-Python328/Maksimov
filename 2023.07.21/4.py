n = input('')
bit_number = int('9' * int(n))
count_num = 0
x = int('1' + '0' * (int(n) - 1))
while x < bit_number:
    n = 1
    check_num = 0
    while n <= x:
        if x % n == 0: 
            check_num += 1
        if (n == x) and (check_num == 2):
            count_num += 1
        n += 1
    x += 1
print(count_num)

#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.33. ДЗ (Циклы, range(), генераторные выражения)>python -i 4.py
#3
#143
#>>>
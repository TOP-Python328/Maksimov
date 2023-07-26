ticket = input('введите номер билета: ')
trhree_sum_one = 0
trhree_sum_two = 0
if len(ticket) == 6: 
    n = 0
    t = 3
    while n < 3:
        trhree_sum_one += int(list(ticket)[n])
        n += 1
    while t < 6:
        trhree_sum_two += int(list(ticket)[t])
        t += 1
    if (trhree_sum_one == trhree_sum_two):
        print('да')
    else:
        print('нет')
else:
    print('номер билета должно иметь шесть цыфр')
    
#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.33. ДЗ (Циклы, range(), генераторные выражения)>python -i 6.py
#введите номер билета: 183534
#да
#>>>

#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.33. ДЗ (Циклы, range(), генераторные выражения)>python -i 6.py
#введите номер билета: 401367
#нет
#>>>
    
    
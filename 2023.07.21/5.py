telegram = input('введите сообщение: ')
code = len(list(telegram.replace(' ', '')))
Rub = int((code * 30) / 100)
Cop = f'{(((code * 30) / 100 - int((code * 30) / 100)) * 100):.0f}'
print(Rub, 'руб.', Cop, 'коп.')

#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.33. ДЗ (Циклы, range(), генераторные выражения)>python -i 5.py
#введите сообщение: грузите апельсины бочках братья карамазовы
#11 руб. 40 коп.
#>>>
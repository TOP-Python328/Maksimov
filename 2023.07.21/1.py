# ПЕРЕИМЕНОВАТЬ: имя array_0 ничего не говорит о содержимом, но ещё и вводит в заблуждение относительно типа данных
array_0 = ''
while True:
    std = input('введите число: ')
    if float(std) % 7 == 0:
        array_0 = std + ' ' + array_0
    else:
        # ИСПРАВИТЬ: эта команда не имеет отношения к циклу, её необходимо убрать из тела цикла и поместить сразу после завершения цикла
        print(array_0)
        break


# УДАЛИТЬ везде: в этом комментарии нет необходимости, такие не нужно добавлять
# C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.33. ДЗ (Циклы, range(), генераторные выражения)>python -i 1.py

# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы после символа # — в большинстве редакторов кода, включая Notepad++, это делает команда "Вкл./Выкл. комментарий"
# введите число: 7
# введите число: 14
# введите число: 21
# введите число: 15
# 21 14 7


# ИТОГ: очень хорошо — 3/3


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода: https://peps.python.org/pep-0008/

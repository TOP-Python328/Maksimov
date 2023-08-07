telegram = input('введите сообщение: ')
# ИСПРАВИТЬ: я так понимаю, вы напрочь пропустили ту часть лекции, где я говорил, что и строки, и списки являются индексируемыми последовательностями
code = len(list(telegram.replace(' ', '')))

# ПЕРЕИМЕНОВАТЬ: в Python для имён классов используется ВерблюжийРегистр, для имён условных констант используется ЗМЕИНЫЙ_ВЕРХНИЙ_РЕГИСТР или СЛИТНЫЙВЕРХНИЙРЕГИСТР — для имён всех прочих объектов используется змеиный_нижний_регистр или слитныйнижнийрегистр
# ИСПРАВИТЬ: оператор целочисленного деления, оператор взятия остатка от деления, встроенная функция divmod() — все они нужны, чтобы сделать код быстро читаемым и более производительным (т.к. работа этих операторов и функций оптимизирована на битовом уровне)
Rub = int((code * 30) / 100)
# ИСПРАВИТЬ: абсолютно алогичное действие: рубли хранить в виде int объекта, а копейки в виде str объекта
Cop = f'{(((code * 30) / 100 - int((code * 30) / 100)) * 100):.0f}'
print(Rub, 'руб.', Cop, 'коп.')


# введите сообщение: грузите апельсины бочках братья карамазовы
# 11 руб. 40 коп.

# ДОБАВИТЬ: тесты с другими входными данными


# ИТОГ: нужно лучше — 2/4

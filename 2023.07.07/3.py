minute = int(input('введите минуты: '))
# ИСПРАВИТЬ: в случае, если вам понадобится проводить дальнейшие вычисления, то данный объект придётся снова преобразовывать в int — это избыточно, лучше сохранить объект в качестве числа, строковое представление числа можно получить в любой момент, это очень быстрая операция
# ИСПРАВИТЬ: используйте оператор целочисленного деления
hour_f1 = f'{int(minute / 60)}'
# ИСПРАВИТЬ: используйте оператор взятия остатка от деления
minute_f1 = f'{minute - int(minute / 60) * 60}'
# ИСПРАВИТЬ: вывод не соответствует требуемому формату (лишние пробелы)
print(minute, ' мин - это ', hour_f1, ' час ', minute_f1, ' мин')


# введите минуты: 150
# 150  мин - это  2  час  30  мин


# ИТОГ: нужно лучше, доработать — 1/3
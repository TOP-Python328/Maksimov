minute = int(input('введите минуты: '))
hour_f1 = f'{int(minute / 60)}'
minute_f1 = f'{minute - int(minute / 60) * 60}'
print(minute,' мин - это ', hour_f1, ' час ',minute_f1, ' мин')

#введите минуты: 150
#150  мин - это  2  час  30  мин
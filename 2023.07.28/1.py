user_mail = input('введите адрес электронной почты: ')

availability_at_sign = 'no'
dot = 'нет'
for char in user_mail:
    if char in '@':
        availability_at_sign = 'yes'
    if char in '.' and availability_at_sign == 'yes':
        dot = 'да'

# КОММЕНТАРИЙ: неплохое решение, однако, согласно условию задачи необходимо было использовать строковые методы — для знакомства с ними и тренировки их использования: обратите внимание на find() и rfind()

print(f'\n{dot}\n')


# введите адрес электронной почты: sgd@ya.ru
#
# да

# введите адрес электронной почты: abcde@fghij
#
# нет


# ИТОГ: переработать — 2/4

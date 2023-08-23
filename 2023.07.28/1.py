user_mail = input('введите адрес электронной почты: ')

# ПЕРЕИМЕНОВАТЬ: символ '@' официально называется "коммерческий ат" (at sign), "собака" — это русское жаргонное название, к dog не имеющее ни малейшего отношения
availability_dog = 'no'
# ПЕРЕИМЕНОВАТЬ: точка (знак препинания) — dot
availability_point = 'нет'
# ПЕРЕИМЕНОВАТЬ: символ (текста) — character, char, ch
for mail_simvol in list(user_mail):
    if mail_simvol in '@':
        availability_dog = 'yes'
    if mail_simvol in '.' and availability_dog == 'yes':
        availability_point = 'да'

print(f'\n{availability_point}\n')


# введите адрес электронной почты: sgd@ya.ru
#
# да

# введите адрес электронной почты: abcde@fghij
#
# нет


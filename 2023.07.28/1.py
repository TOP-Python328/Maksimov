user_mail = input('введите адрес электронной почты: ')

availability_dog = 'no'
availability_point = 'нет'
for mail_simvol in list(user_mail):
    if mail_simvol in '@':
        availability_dog = 'yes'
    if mail_simvol in '.' and availability_dog == 'yes':
        availability_point = 'да'

print(f'\n{availability_point}\n')

#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.07.28>python -i 1.py
#введите адрес электронной почты: sgd@ya.ru

#да

#>>> ^Z


#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.07.28>python -i 1.py
#введите адрес электронной почты: abcde@fghij

#нет

#>>>

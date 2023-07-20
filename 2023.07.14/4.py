import sys

std = sys.stdin.readlines()
stdO = sys.stdout

motion_1 = list(std[0])
motion_2 = list(std[1])

motion_1_result = ''
motion_2_result = ''

if motion_1[0] == 'a' or motion_1[0] == 'c' or motion_1[0] == 'e' or motion_1[0] == 'g':
    if motion_1[1] == '8' or motion_1[1] == '6' or motion_1[1] == '4' or motion_1[1] == '2':
        motion_1_result = 'white'
    else:
        motion_1_result = 'black'
else:
    if motion_1[1] == '8' or motion_1[1] == '6' or motion_1[1] == '4' or motion_1[1] == '2':
        motion_1_result = 'black'
    else:
        motion_1_result = 'white'


if (motion_2[0] == 'a' or motion_2[0] == 'c' or motion_2[0] == 'e' or motion_2[0] == 'g'):
    if (motion_2[1] == '8' or motion_2[1] == '6' or motion_2[1] == '4' or motion_2[1] == '2'):
        motion_2_result = 'white'
    else:
        motion_2_result = 'black'
else:
    if (motion_2[1] == '8' or motion_2[1] == '6' or motion_2[1] == '4' or motion_2[1] == '2'):
        motion_2_result = 'black'
    else:
        motion_2_result = 'white'

if (motion_1_result == 'white' and motion_2_result == 'white') or (motion_1_result == 'black' and motion_2_result == 'black'):
    stdO.write('да')
else:
    stdO.write('нет')
    
    
#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.31. ДЗ (Условные конструкции, логические операторы, индексация)>python -i 4.py
#e5
#g4
#^Z
#нет>>> ^Z


#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.31. ДЗ (Условные конструкции, логические операторы, индексация)>python -i 4.py
#b1
#g8
#^Z
#да>>> ^Z


#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.31. ДЗ (Условные конструкции, логические операторы, индексация)>python -i 4.py
#d8
#c3
#^Z
#да>>>
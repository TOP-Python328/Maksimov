import sys

sdt = sys.stdin.readlines()
sdtO = sys.stdout

motion_1 = list(sdt[0])
motion_2 = list(sdt[1])
motion_result = ''

if motion_1[0] == motion_2[0]:
    motion_result = 'да'
else:
    if motion_1[1] == motion_2[1]:
        motion_result = 'да'
    else:
        motion_result = 'нет'
        
sdtO.write(motion_result)

#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.31. ДЗ (Условные конструкции, логические операторы, индексация)>python -i 5.py
#b5
#c6
#^Z
#нет>>> ^Z


#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.31. ДЗ (Условные конструкции, логические операторы, индексация)>python -i 5.py
#b8
#d8
#^Z
#да>>> ^Z


#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.31. ДЗ (Условные конструкции, логические операторы, индексация)>python -i 5.py
#f7
#f3
#^Z
#да>>>
import sys

std = sys.stdin.readlines()
stdO = sys.stdout

motion_1 = list(std[0])
motion_2 = list(std[1])
motion_result = ''

letter_coordinate = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

x = motion_1[0]
y = motion_2[0]

if (letter_coordinate[x] - letter_coordinate[y]) == 1 or (letter_coordinate[x] - letter_coordinate[y]) == -1 or (letter_coordinate[x] - letter_coordinate[y]) == 0:
    if (int(motion_1[1]) - int(motion_2[1])) == 1 or (int(motion_1[1]) - int(motion_2[1])) == -1 or (int(motion_1[1]) - int(motion_2[1])) == 0:
        motion_result = 'да'
    else:
        motion_result = 'нет'
else:
    motion_result = 'нет'
    
stdO.write(motion_result)

#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.31. ДЗ (Условные конструкции, логические операторы, индексация)>python -i 6.py
#g3
#f2
#^Z
#да>>> ^Z


#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.31. ДЗ (Условные конструкции, логические операторы, индексация)>python -i 6.py
#c6
#d4
#^Z
#нет>>>
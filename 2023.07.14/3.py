import sys

std = sys.stdin.readlines()
stdO = sys.stdout

multiple_4 = float(float(int(std[0]) / 4) - int(int(std[0]) / 4))
multiple_100 = float(float(int(std[0]) / 100) - int(int(std[0]) / 100))

if multiple_4 == 0 and multiple_100 != 0:
    stdO.write('да')
else:
    stdO.write('нет')
    
#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.31. ДЗ (Условные конструкции, логические операторы, индексация)>python -i 3.py
#2011
#^Z
#нет>>> ^Z


#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.31. ДЗ (Условные конструкции, логические операторы, индексация)>python -i 3.py
#2012
#^Z
#да>>>

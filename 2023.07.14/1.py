import sys

std = sys.stdin.readlines()

num_1_1, num_1_2, num_1_3 = int(std[0]), int(std[1]), int(std[2])
num_1_0 = 0

if (num_1_1 >= 0):
    num_1_0 += num_1_1
if (num_1_2 >= 0):
    num_1_0 += num_1_2
if (num_1_3 >= 0):
    num_1_0 += num_1_3

print(num_1_0)

#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\Д.31. ДЗ (Условные конструкции, логические операторы, индексация)>python -i 1.py
#5
#6
#-7
#^Z
#11
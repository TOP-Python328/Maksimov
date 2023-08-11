files = input('Введите наименования файлов: ')

files = list(files.split('; '))
midle_file = []
final_file = []

for fi_ in files:
    midle_file.append(fi_)
    if midle_file.count(fi_) > 1:
        c = midle_file.count(fi_)
        fi_ = list(fi_)
        fi_.reverse()
        point_indicator = False
        for i in range(len(fi_)):
            if fi_[i - 1] == '.' and point_indicator == False:
                point_indicator = True
                fi_[i - 1] = '_' + str(c) + '.'   
        fi_.reverse()
        fi_ = ''.join(fi_)
        final_file.append(fi_)
    else:
        final_file.append(fi_)
for ff in final_file:
    print(ff)


# C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.07.28>python -i 8.py
# Введите наименования файлов: 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# 1.py
# 1_2.py
# src.tar.gz
# aux.h
# main.cpp
# functions.h
# main_2.cpp
# 1_3.py
# main_3.cpp
# src.tar_2.gz
# >>>
files = input('Введите наименования файлов: ')
files = list(files.split('; '))

midle_file = []
final_file = []

# ПЕРЕИМЕНОВАТЬ: файл — file
# Замечания исправлены__________________________________
for file in files:
    midle_file.append(file)
    if midle_file.count(file) > 1:
        # ПЕРЕИМЕНОВАТЬ: счётчик — counter, cnt
        # Замечания исправлены__________________________________
        counter = midle_file.count(file)
        file = list(file)
        file.reverse()
        point_indicator = False
        for i in range(len(file)):
            if file[i-1] == '.' and point_indicator == False:
                point_indicator = True
                file[i-1] = '_' + str(counter) + '.'
        file.reverse()
        file = ''.join(file)
        final_file.append(file)
    else:
        final_file.append(file)

for ff in final_file:
    print(ff)


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


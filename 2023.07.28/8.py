files = input('Введите наименования файлов: ')
# ИСПРАВИТЬ: строковый метод split() всегда возвращает объект list — преобразование в list избыточно
files = list(files.split('; '))

# ПЕРЕИМЕНОВАТЬ: file — файл (ед.ч.); files — файлы (мн.ч.)
# КОММЕНТАРИЙ: текущие имена списков могут навести на мысль, что в каждом списке находится содержимое одного файла — необходимо давать переменным более однозначные имена
midle_file = []
final_file = []

# ИСПРАВИТЬ: вместо использования двух списков куда более продуктивно создать множество из имён файлов, по которому затем итерироваться, а количество файлов проверять в исходном списке файлов
for file in files:
    midle_file.append(file)
    if midle_file.count(file) > 1:
        counter = midle_file.count(file)
        # ИСПРАВИТЬ: для получения строки в обратном направлении достаточно взять срез [::-1] — от конца строки до начала строки с шагом -1
        file = list(file)
        file.reverse()
        # ИСПРАВИТЬ: используйте срезы строк и строковые методы вместо явного использования логических переменных и цикла
        point_indicator = False
        for i in range(len(file)):
            # ИСПРАВИТЬ: после ключевых слов if и elif интерпретатор ожидает объект bool, а не оператор сравнения — вам не нужно сравнивать объект bool с объектом False
            if file[i-1] == '.' and point_indicator == False:
                point_indicator = True
                file[i-1] = '_' + str(counter) + '.'
        file.reverse()
        file = ''.join(file)
        # ИСПРАВИТЬ: данное действие выполняется одинаковым образом вне зависимости от результата проверки условия — вынести за пределы условной конструкции
        final_file.append(file)
    else:
        final_file.append(file)

# ИСПРАВИТЬ: условие задачи требует вывести новые имена файлов по алфавиту
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


# ИТОГ: переработать — 2/6


# ИСПОЛЬЗОВАТЬ: изучите более оптимальный вариант решения
files = input().split('; ')
files_renamed = []
for file in set(files):
    for cnt in range(1, files.count(file)+1):
        suffix = f'_{cnt}.' if cnt > 1 else '.'
        files_renamed.append(suffix.join(file.split('.', 1)))
print(*sorted(files_renamed), sep='\n')

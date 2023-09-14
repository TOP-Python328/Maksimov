from sys import path
from pathlib import Path
from utils import load_file

def ask_for_file() -> 'module':
    """Функция которая запрашивает у пользователя путь к потерянному файлу и копирует этот файл с помощью функции load_file"""
    while True:
        file_path = Path(path[0]) / input('путь: ')
        if file_path.exists():
            break
        else:
            print('! по указанному пути отсутствует необходимый файл !')
    datafile_path = load_file(file_path)
    import copy_conf
    
    # with open(datafile_path, encoding='utf-8') as filein:
        # defaults = filein.read()
    return copy_conf

# >>> config_module = ask_for_file()
# путь: C:\Users\user\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.09.03\conf.py
# ! по указанному пути отсутствует необходимый файл !
# путь: C:\Users\user\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.09.03\data\conf.py
# >>>
# >>> config_module.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}
from sys import path
from pathlib import Path
import datetime

def logger(func_obj: 'function'):
    """Декоратор который в файле function_calls.log ведёт журнал вызовов декорируемой функции"""

    dt = datetime.datetime.now()
    new_dt = dt.strftime('%Y.%m.%d %H:%M:%S')
    
    file_fun_calls = Path(path[0]) / ('data/function_calls.log')
    def wrapper(*args, **kwargs): 
        name_fun = func_obj.__name__ # Имя функции
    
        args_obj = list(args) # Аргументы без ключей
        args_obj = list(map(str, args_obj))
        
        kwargs_obj = list() # Аргументы с ключами
        for k, v in kwargs.items():
            kwargs_obj.append(str(k) + '=' + str(v))
        
        try: # результат произвольной функции
            result = f'-> {func_obj(*args, **kwargs)}'
        except Exception as exception:
            result = f'.. {type(exception).__name__}: {str(exception)}'
        
        with open(file_fun_calls, 'a', encoding='utf-8') as filein:
            filein.write(f'{new_dt} - {name_fun}({", ".join(args_obj + kwargs_obj)}) {result}\n')
        print(f'{func_obj(*args, **kwargs)}')
    return wrapper

# C:\Users\user\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.09.03>python -i 5.py
# >>>
# >>> def div_round(num1, num2, *, digits=0):
# ...      return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>> div_round(2, 3, digits=2)
# 0.67
# >>> ^Z

# C:\Users\user\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.09.03\data\function_calls.log
# 2023.09.15 11:42:25 - div_round(2, 3, digits=2) -> 0.67

# C:\Users\user\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.09.03>python -i 5.py
# >>>
# >>> def testing_function():
# ...     pass
# ...
# >>> testing_function = logger(testing_function)
# >>> testing_function()
# None
# >>> ^Z

# C:\Users\user\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.09.03\data\function_calls.log
# 2023.09.15 11:54:27 - div_round(2, 3, digits=2) -> 0.67
# 2023.09.15 11:54:41 - testing_function() -> None



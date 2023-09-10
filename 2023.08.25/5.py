def logger(func_obj: 'function'):
    def wrapper(*args, **kwargs): 
        name_fun = func_obj.__name__ # Имя функции
    
        args_obj = list(args) # Аргументы без ключей
        args_obj = list(map(str, args_obj))
        
        kwargs_obj = list() # Аргументы с ключами
        for k, v in kwargs.items():
            kwargs_obj.append(str(k) + '=' + str(v))
        
        try: # результат произвольной функции
            result = f'-> {func_obj(*args, **kwargs)}\n{func_obj(*args, **kwargs)}'
        except Exception as exception:
            result = f'.. {type(exception).__name__}: {str(exception)}'
        
        print(f'{name_fun}({", ".join(args_obj + kwargs_obj)}) {result}')

    return wrapper
    
# >>> def div_round(num1, num2, *, digits=0):
# ...     return round(num1 / num2, digits)
# ...
# >>> div_round = logger(div_round)
# >>>
# >>>
# >>> div_round(1, 3, digits=2)
# div_round(1, 3, digits=2) -> 0.33
# 0.33
# >>> div_round(7, 2)
# div_round(7, 2) -> 4.0
# 4.0
# >>> div_round(5, 0)
# div_round(5, 0) .. ZeroDivisionError: division by zero
# ДОБАВИТЬ: параметризация декораторов осуществляется через ещё одну обёртку
def repeat(fun_obj: 'function') -> 'function':
    """Параметризуемый декоратор который выполняет декорируемую функцию заданное количество раз"""
    # КОММЕНТАРИЙ: с такой сигнатурой функции-оболочки вы потеряли возможность декорировать функции с различными наборами аргументов (см. тест ниже)
    def wrapper(num_calls: int = 2):
        for _ in range(num_calls):
            fun_obj()
    return wrapper


# >>> def testing_function():
# ...     print('python')
# ...
# КОММЕНТАРИЙ: это не декорирование: в testing_function оказывается объект None, а не объект функции
# >>> testing_function = repeat(testing_function)(4)
# python
# python
# python
# python
# >>>
# >>> testing_function()
# ...
# TypeError: 'NoneType' object is not callable

# >>> def testing_function_2(n1, n2):
# ...     return n1 * n2
# ...
# КОММЕНТАРИЙ: вот это декорирование: но здесь у нас нет возможности указать количество повторов для декоратора
# >>> testing_function_2 = repeat(testing_function_2)
# >>>
# КОММЕНТАРИЙ: а вызов срывается, потому что оболочка оказывается не в состоянии принять два аргумента
# >>> testing_function_2(1, 2)
# ...
# TypeError: repeat.<locals>.wrapper() takes from 0 to 1 positional arguments but 2 were given


# ИТОГ: нужно лучше, переделать — 1/5

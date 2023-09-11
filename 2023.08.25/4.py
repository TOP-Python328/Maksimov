def repeat(fun_obj: 'function') -> 'function':
    def wrapper(num_calls: int=2):
        for n in range(num_calls):
            fun_obj()
    return wrapper
    
# >>> def testing_function():
# ...     print('python')
# ...
# >>> testing_function = repeat(testing_function)(4)
# python
# python
# python
# python
# >>>
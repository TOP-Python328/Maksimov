from functools import wraps
from time import sleep

def exception_delay_repeat(func: 'function') -> 'function':
    @wraps(func)
    def wrapper():
        try:
            return func()
        except Exception as ex:
            sleep(0.5)
            print('ConnectionError: ', ex)
            return None
    
    return wrapper
    
# >>> from random import randrange
# >>>
# >>> def test_func():
# ...     if randrange(2):
# ...         raise ConnectionError('failure')
# ...     else:
# ...         return 'success'
# ...
# >>> test_func
# <function test_func at 0x00000159BFCB82C0>
# >>>
# >>> test_func = exception_delay_repeat(test_func)
# >>> test_func
# <function test_func at 0x00000159BFCF13A0>
# >>>
# >>> test_func()
# 'success'
# >>> test_func()
# ConnectionError:  failure
# >>> test_func()
# 'success'
# >>> test_func()
# ConnectionError:  failure
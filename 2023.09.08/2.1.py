from collections.abc import Iterable

def product(numbers: Iterable[float]) -> sum:
    """Функция которая возвращает произведение чисел"""
    composition = 0
    for x in numbers:
        if numbers.index(x) > 0:
            composition = composition * x
        else:
            composition = x
    if composition == -0: composition = 0
    
    return composition

# >>> product(range(10, 60, 10))
# 12000000
# >>>
# >>> product((0.12, 0.05, -0.09, 0.0, 0.21))
# 0
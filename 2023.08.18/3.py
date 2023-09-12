# ИСПРАВИТЬ: функция возвращает список вещественных чисел, а не произвольных объектов — это должно быть отражено в аннотации
def numbers_strip(numbers: list[float], n: int=1, copy_: bool=False) -> list[float]:
    """Функция удаляет n минимальных и n максимальных чисел из списка"""
    # если copy=False то функция возвращает итерированный исходный объект;
    # если copy=True то функция возвращает копию исходного объекта;
    if copy_:
        numbers = numbers.copy()

    for _ in range(n): # Удаление Максимальных и минимальных значений
        numbers.remove(min(numbers))
        numbers.remove(max(numbers))
    return numbers


# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True
# >>> id(sample)
# 2339904526720
# >>> id(sample_stripped)
# 2339904526720
# >>>
# >>> sample = [10, 20, 30, 40, 50]
# >>> sample_stripped = numbers_strip(sample, 2, copy_=True)
# >>> sample_stripped
# [30]
# >>> sample is sample_stripped
# False
# >>> id(sample)
# 2339904525824
# >>> id(sample_stripped)
# 2339904524480
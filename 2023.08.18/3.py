# ИСПРАВИТЬ: параметр copy должен быть строго ключевым
# ИСПРАВИТЬ: функция возвращает список вещественных чисел, а не произвольных объектов — это должно быть отражено в аннотации
def numbers_strip(numbers: list[float], n: int=1, copy=False) -> list:
    # ДОБАВИТЬ: документацию функции
    if copy: # если copy=True то функция возвращает копию исходного объекта;
        # ПЕРЕИМЕНОВАТЬ: используйте идентификатор numbers
        work_object = numbers.copy()
    # УДАЛИТЬ: данный блок избыточен
    else: # если copy=False то функция возвращает итерированный исходный объект;
        work_object = numbers
    
    for _ in range(n): # Удаление Максимальных и минимальных значений
        work_object.remove(min(work_object))
        work_object.remove(max(work_object))
    return work_object


# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True
# >>> id(sample)
# 2966653841600
# >>> id(sample_stripped)
# 2966653841600
# >>>
# >>> sample = [10, 20, 30, 40, 50]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped
# [30]
# >>> sample is sample_stripped
# False
# >>> id(sample)
# 2966653840704
# >>> id(sample_stripped)
# 2966653839360
# >>>


# ИТОГ: нужно лучше, доработать — 1/4

# КОММЕНТАРИЙ: минус балл за несоблюдение требований оформления в соответствии с PEP 8 — несмотря на многочисленные указания и примеры, предоставленные преподавателем

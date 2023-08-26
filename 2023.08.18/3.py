def numbers_strip(numbers: list[float], n: int=1, copy=False) -> list:
    if copy: # если copy=True то функция возвращает копию исходного объекта;
        work_object = numbers.copy()
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
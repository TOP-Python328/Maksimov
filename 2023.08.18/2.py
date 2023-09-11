def taxi_cost(path_length: int, waiting_time: int = 0) -> int | None:
    # ДОБАВИТЬ: документацию функции
    price_for_150_meters = (path_length / 150) * 6 # расчет дополнительных 6-ти рублей за 150 метров поездки;
    the_price_for_waiting = waiting_time * 3 # расчет дополнительных 3-х рублей за минуту ожидания;
    if path_length == 0: # штраф 80 рублей за отмененный заказ;
        fine = 80
    else:
        fine = 0
    # ИСПРАВИТЬ: данное условие должно располагаться в начале тела функции
    # ДОБАВИТЬ: ещё одно условие возврата None (см. тест ниже)
    if path_length < 0: # Проверка на отрицательный ввод длины маршрута;
        return None
    else: # Итоговый расчет стоимости маршрута;
        return round(80 + price_for_150_meters + the_price_for_waiting + fine)


# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))
# None

# >>> print(taxi_cost(1500, -10))
# КОММЕНТАРИЙ: должно быть None
# 110


# ИТОГ: нужно лучше, доработать — 1/4

# КОММЕНТАРИЙ: минус балл за несоблюдение требований оформления в соответствии с PEP 8 — несмотря на многочисленные указания и примеры, предоставленные преподавателем

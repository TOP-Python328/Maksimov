import math
def taxi_cost(path_length: int, waiting_time: int = 0) -> int | None:
    if path_length < 0:
        return None
    else:
        price_for_150_meters = int(math.floor(path_length / 150) * 6)
        the_price_for_waiting = int(waiting_time * 3)
        if path_length == 0:
            fine = 80
        else:
            fine = 0
        return (80 + price_for_150_meters + the_price_for_waiting + fine)
        
#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.08.18>python -i 2.py
#>>> taxi_cost(1500)
#140
#>>> taxi_cost(2560)
#182
#>>> taxi_cost(0, 5)
#175
#>>> taxi_cost(42130, 8)
#1784
#>>> print(taxi_cost(-300))
#None
#>>>
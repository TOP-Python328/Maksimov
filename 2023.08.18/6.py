def orth_triangle(cathetus1 = 0, cathetus2 = 0, hypotenuse = 0) -> float | None:
    """Функция вычисляет третью сторону прямоугольного треугольника по двум переданным"""
    # Проверка на возможность вычисления по Теореме Пифагора;
    if (
        cathetus1 > hypotenuse > 0 and cathetus1 > 0
        or cathetus2 > hypotenuse > 0 and cathetus2 > 0
        or cathetus1 != 0 and cathetus2 != 0 and hypotenuse != 0
        ):
        return None
    elif not hypotenuse: # Расчет при известных переменных cathetus1 и cathetus2;
        hypotenuse = (cathetus1**2 + cathetus2**2)**(1 / 2)
        return hypotenuse
    elif not cathetus1: # Расчет при известных переменных cathetus2 и hypotenuse;
        cathetus1 = (hypotenuse**2 - cathetus2**2)**(1 / 2)
        return cathetus1
    elif not cathetus2: # Расчет при известных переменных cathetus1 и hypotenuse;
        cathetus2 = (hypotenuse**2 - cathetus1**2)**(1 / 2)
        return cathetus2


# >>> orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None
# >>> print(orth_triangle(cathetus2=-2, hypotenuse=3))
# 2.23606797749979
# >>> print(orth_triangle(cathetus1=1, cathetus2=2, hypotenuse=3))
# None

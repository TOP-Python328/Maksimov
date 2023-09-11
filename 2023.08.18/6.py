# ИСПРАВИТЬ: все параметры функции должны быть строго ключевыми
def orth_triangle(cathetus1: float=0, cathetus2: float=0, hypotenuse: float=0,) -> float | None:
    # ДОБАВИТЬ: документацию функции
    # ИСПРАВИТЬ: высокую степень избыточности в формулировке условий
    if (cathetus1 < 0 # Проверка на возможность вычисления по Теореме Пифагора;
        or cathetus2 < 0
        or hypotenuse < 0
        or hypotenuse < cathetus1 and hypotenuse > 0 and cathetus1 > 0
        or hypotenuse < cathetus2 and hypotenuse > 0 and cathetus2 > 0
        or cathetus1 != 0 and cathetus2 != 0 and hypotenuse != 0
        ):
        return None
    elif not hypotenuse: # Расчет при известных переменных cathetus1 и cathetus2;
        hypotenuse = (cathetus1 ** 2 + cathetus2 ** 2) ** (1 / 2)
        return hypotenuse
    elif not cathetus1: # Расчет при известных переменных cathetus2 и hypotenuse;
        cathetus1 = (hypotenuse ** 2 - cathetus2 ** 2) ** (1 / 2)
        return cathetus1
    elif not cathetus2: # Расчет при известных переменных cathetus1 и hypotenuse;
        cathetus2 = (hypotenuse ** 2 - cathetus1 ** 2) ** (1 / 2)
        return cathetus2


# >>> orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None
# >>> print(orth_triangle(cathetus2=-2, hypotenuse=3))
# None
# >>> print(orth_triangle(cathetus1=1, cathetus2=2, hypotenuse=3))
# None


# ИТОГ: нужно лучше, доработать — 1/4

# КОММЕНТАРИЙ: минус балл за несоблюдение требований оформления в соответствии с PEP 8 — несмотря на многочисленные указания и примеры, предоставленные преподавателем

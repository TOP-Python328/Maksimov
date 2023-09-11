def strong_password(password: str) -> bool:
    # ДОБАВИТЬ: документацию функции
    upper_case = False # Вычисление латинских букв нижнего регистра в пароле;
    for simvol in password:
        # ИСПРАВИТЬ: оператор and избыточен — в Python возможно конструировать цепочки сравнительных операторов
        # ИСПРАВИТЬ: многократный вызов функции ord() на каждой итерации цикла избыточен, замедляет выполнение кода
        if ord(simvol) >= 65 and ord(simvol) <= 90:
            upper_case = True
            break
    lowercase = False # Вычисление латинских букв ВЕРХНЕГО регистра в пароле;
    # УДАЛИТЬ: повторное итерирование по строке избыточно, сильно замедляет выполнение кода, необходимо обойтись одним циклом
    for simvol in password:
        if ord(simvol) >= 97 and ord(simvol) <= 122:
            lowercase = True
            break
    counting_numbers = 0 # Подсчет количества цифр в пароле;
    for simvol in password:
        if ord(simvol) >= 48 and ord(simvol) <= 57:
            counting_numbers += 1
    other_signs = False # Вычисление символов прочих категорий (пробел, знаки пунктуации, диакритические знаки и т.п.);
    for simvol in password:
        if (ord(simvol) >= 32 and ord(simvol) <= 47
            or ord(simvol) >= 58 and ord(simvol) <= 64
            or ord(simvol) >= 91 and ord(simvol) <= 96
            or ord(simvol) >= 123 and ord(simvol) <= 126
        ):
            other_signs = True
            break
    # КОММЕНТАРИЙ: рекомендовано использование встроенной функции all()
    if len(password) < 8: # Проверка длины пароля (менее восьми);
        return False
    # ИСПРАВИТЬ: данный блок повторяет предыдущий, составьте условия таким образом, чтобы блоки не дублировали друг друга
    elif upper_case == False: # Проверка на отсутствие латинских букв ВЕРХНЕГО регистра;
        return False
    elif lowercase == False: # Проверка на отсутствие латинских букв нижнего регистра;
        return False
    elif counting_numbers < 2: # Проверка на отсутствие двух или более цифр;
        return False
    elif other_signs == False: # Проверка на отсутствие символов прочих категорий (пробел, знаки пунктуации, диакритические знаки и т.п.);
        return False
    elif other_signs: # Проверка на НАЛИЧИЕ символов прочих категорий (пробел, знаки пунктуации, диакритические знаки и т.п.);
        return True


# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('password')
# False
# >>>


# ИТОГ: переделать — 1/6

# КОММЕНТАРИЙ: минус балл за несоблюдение требований оформления в соответствии с PEP 8 — несмотря на многочисленные указания и примеры, предоставленные преподавателем

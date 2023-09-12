def strong_password(password: str) -> bool:
    """Функция проверяет надежность пароля"""
    upper_case = False # Вычисление латинских букв нижнего регистра в пароле;
    lowercase = False # Вычисление латинских букв ВЕРХНЕГО регистра в пароле;
    counting_numbers = [0, False] # Подсчет количества цифр в пароле;
    other_signs = False # Вычисление символов прочих категорий (пробел, знаки пунктуации, диакритические знаки и т.п.);
    for simvol in password:
        simvol = ord(simvol)
        if 32 <= simvol <= 126:
            upper_case = True
        if 97 <= simvol <= 122:
            lowercase = True
        if 48 <= simvol <= 57:
            counting_numbers[0] += 1
            if counting_numbers[0] >= 2: 
                counting_numbers[1] = True
        if (32 <= simvol <= 47
            or 58 <= simvol <= 64
            or 91 <= simvol <= 96
            or 123 <= simvol <= 126
        ):
            other_signs = True

    return all([len(password) >= 8, upper_case,
                lowercase, counting_numbers[1],
                other_signs])
 
# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('password')
# False
# >>>


# ИТОГ: переделать — 1/6

# КОММЕНТАРИЙ: минус балл за несоблюдение требований оформления в соответствии с PEP 8 — несмотря на многочисленные указания и примеры, предоставленные преподавателем

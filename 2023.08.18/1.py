def strong_password(password: str) -> bool:

    upper_case = False # Вычисление латинских букв нижнего регистра в пароле;
    for simvol in password:
        if ord(simvol) >= 65 and ord(simvol) <= 90:
            upper_case = True
            break
    lowercase = False # Вычисление латинских букв ВЕРХНЕГО регистра в пароле;
    for simvol in password:
        if ord(simvol) >= 97 and ord(simvol) <= 122:
            lowercase = True
            break
    counting_numbers = 0 # Подсчет количества цыфр в пароле;
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

    if len(password) < 8: # Проверка длины пароля (менее восьми);
        return False
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
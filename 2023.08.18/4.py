def countable_nouns(num: int, tuple_of_nouns: tuple[str, str, str]) -> str:
    """Функция возвращающая существительное русского языка, согласованное с числом"""

    if num == (num // 10)*10 + 1 and num != (num // 100)*100 + 11: # согласование с первым вариантов существительных;
        return tuple_of_nouns[0]
        
    elif (2 <= num <= 4 # согласование со вторым вариантов существительных;
          num - 4 <= (num // 20) * 20 <= num - 2 
        ):
        return tuple_of_nouns[1]
        
    else: # согласование с третьим вариантов существительных;
        return tuple_of_nouns[2]


# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(111, ("год", "года", "лет"))
# 'лет'
# >>>
# >>> countable_nouns(31, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(451, ("год", "года", "лет"))
# 'год'
# >>>
# >>> countable_nouns(343, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(344, ("год", "года", "лет"))
# 'года'
# >>>
# >>> countable_nouns(675, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(676, ("год", "года", "лет"))
# 'лет'
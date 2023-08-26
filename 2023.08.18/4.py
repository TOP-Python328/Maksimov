def countable_nouns(first_argument: int, tuple_of_nouns: tuple[str, str, str,]) -> str:
    if first_argument == (first_argument // 10) * 10 + 1 and first_argument != 11: # согласование с первым вариантов существительных;
        return tuple_of_nouns[0]
        
    elif (first_argument >= 2 and first_argument <= 4 # согласование со вторым вариантов существительных;
        or 
          first_argument >= (first_argument // 20) * 20 + 2 and first_argument <= (first_argument // 20) * 20 + 4
        ):
        return tuple_of_nouns[1]
        
    else: # согласование с третьим вариантов существительных;
        return tuple_of_nouns[2]
        
# 'год'
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

# >>> countable_nouns(21, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(31, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(451, ("год", "года", "лет"))
# 'год'

# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(3, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(4, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(23, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(24, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(342, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(343, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(344, ("год", "года", "лет"))
# 'года'

# >>> countable_nouns(0, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(5, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(6, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(7, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(8, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(9, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(11, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(13, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(14, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(15, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(16, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(17, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(18, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(19, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(20, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(25, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(26, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(27, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(28, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(29, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(30, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(35, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(675, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(676, ("год", "года", "лет"))
# 'лет'
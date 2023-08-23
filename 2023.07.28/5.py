scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

word = input('введите слово: ')
# ПЕРЕИМЕНОВАТЬ: очки, счёт (в игре) — score, scores, points
point = 0
# ПЕРЕИМЕНОВАТЬ: очки, счёт (в игре) — score, scores, points
for k in list(scores_letters.keys()):
    # ПЕРЕИМЕНОВАТЬ: символ (текста) — character, char, ch
    for n in list(word):
        # ПЕРЕИМЕНОВАТЬ: is_char_in_letters
        # ИСПОЛЬЗОВАТЬ везде: круглые скобки используются для литерала кортежа, изменения порядка вычисления выражений, вызова функций и записи составного выражения на нескольких строчках — больше нигде и никак
        gen_point = {n.upper()} < set(scores_letters[k])
        if gen_point == True:
            point += int(k)
print(f'\n{point}\n')


# введите слово: синхрофазотрон
#
# 29


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
points = 0
for score in list(scores_letters.keys()):
    for ch in list(word):
        is_char_in_letters = {ch.upper()} < set(scores_letters[score])
        if is_char_in_letters == True:
            points += int(score)
print(f'\n{points}\n')


# введите слово: синхрофазотрон
#
# 29


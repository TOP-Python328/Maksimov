word = input('введите слово: ')

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

point = 0

for k in list(scores_letters.keys()):
    for n in list(word):
        gen_point = ({n.upper()} < set(scores_letters[k]))
        if gen_point == True:
            point += int(k)
print(f'\n{point}\n')

#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.07.28>python -i 5.py
#введите слово: синхрофазотрон

#29

#>>>
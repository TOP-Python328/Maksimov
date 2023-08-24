fruits = list()
fruits_answer = str()
while True:
    fruit = input('название фрукта: ')
    if fruit != '':
        fruits.append(fruit)
    else:
        i = 0
        while i != len(fruits):
            if i == len(fruits) - 1:
                fruits_answer += (fruits[i])
            if i == len(fruits) - 2:
                fruits_answer += (fruits[i] + ' и ')
            if i < len(fruits) - 2:
                fruits_answer += (fruits[i] + ', ')
            i += 1
        break
            
print(f'\n{fruits_answer}\n')


# название фрукта: яблоко
# название фрукта:
#
# яблоко

# название фрукта: яблоко
# название фрукта: груша
# название фрукта:
#
# яблоко и груша

# название фрукта: яблоко
# название фрукта: груша
# название фрукта: апельсин
# название фрукта:
#
# яблоко, груша и апельсин


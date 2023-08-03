import sys

std = sys.stdin.readlines()
stdO = sys.stdout

# УДАЛИТЬ: объекты str также являются индексируемыми
motion_1 = list(std[0])
motion_2 = list(std[1])

motion_1_result = ''
motion_2_result = ''

# ИСПРАВИТЬ: здесь и далее уместнее использовать оператор проверки принадлежности in
if motion_1[0] == 'a' or motion_1[0] == 'c' or motion_1[0] == 'e' or motion_1[0] == 'g':
    if motion_1[1] == '8' or motion_1[1] == '6' or motion_1[1] == '4' or motion_1[1] == '2':
        motion_1_result = 'white'
    else:
        motion_1_result = 'black'
else:
    if motion_1[1] == '8' or motion_1[1] == '6' or motion_1[1] == '4' or motion_1[1] == '2':
        motion_1_result = 'black'
    else:
        motion_1_result = 'white'

# ИСПРАВИТЬ: лишние скобки
if (motion_2[0] == 'a' or motion_2[0] == 'c' or motion_2[0] == 'e' or motion_2[0] == 'g'):
    # ИСПРАВИТЬ: лишние скобки
    if (motion_2[1] == '8' or motion_2[1] == '6' or motion_2[1] == '4' or motion_2[1] == '2'):
        motion_2_result = 'white'
    else:
        motion_2_result = 'black'
else:
    # ИСПРАВИТЬ: лишние скобки
    if (motion_2[1] == '8' or motion_2[1] == '6' or motion_2[1] == '4' or motion_2[1] == '2'):
        motion_2_result = 'black'
    else:
        motion_2_result = 'white'

# СДЕЛАТЬ: подумайте о закономерности в расположении чёрных и белых клеток на доске, и о том, как можно эту закономерность математически рассчитать — данную задачу можно решить куда более изящно

# ИСПРАВИТЬ: для нахождения совпадения или различия достаточно сравнить между собой motion_1_result и motion_2_result
if (motion_1_result == 'white' and motion_2_result == 'white') or (motion_1_result == 'black' and motion_2_result == 'black'):
    stdO.write('да')
else:
    stdO.write('нет')


# e5
# g4
# ^Z
# нет>>> ^Z

# b1
# g8
# ^Z
# да>>> ^Z

# d8
# c3
# ^Z
# да>>>


# ИТОГ: работает, но можно лучше — 2/3

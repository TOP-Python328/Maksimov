import sys

sdt = sys.stdin.readlines()
sdtO = sys.stdout

# УДАЛИТЬ: объекты str также являются индексируемыми
motion_1 = list(sdt[0])
motion_2 = list(sdt[1])

motion_result = ''
if motion_1[0] == motion_2[0]:
    motion_result = 'да'
else:
    # ИСПРАВИТЬ: используйте блок elif или логический оператор or — оба варианта предпочтительнее независимой вложенной условной конструкции
    if motion_1[1] == motion_2[1]:
        motion_result = 'да'
    else:
        motion_result = 'нет'

sdtO.write(motion_result)


# b5
# c6
# ^Z
# нет>>> ^Z

# b8
# d8
# ^Z
# да>>> ^Z

# f7
# f3
# ^Z
# да>>>


# ИТОГ: хорошо, но можно лучше — 2/3

from sys import path
from pathlib import Path
from random import randrange
from datetime import date, timedelta

names = list()

def load_data() -> None:
    """Функция которая читает из файлов данные и упорядочивает их"""
    new_names = Path(path[0]) / 'name.txt'
    with open(new_names, encoding='utf-8') as filein:
        working_list = filein.read()
        working_list = working_list.split('\n')
        for _ in range(len(working_list)):
            rn = randrange(len(working_list) - 1)
            names.append(['', '', '', ''])
            names[-1][0] = working_list[rn]
            if names[-1][0][-1] == '+':
                names[-1][3] = 'женский'
                names[-1][0] = names[-1][0].rstrip('+')
            else:
                names[-1][3] = 'мужской'
 
    new_names = Path(path[0]) / 'patronymic.txt'
    with open(new_names, encoding='utf-8') as filein:
        working_list = filein.read()
        working_list = working_list.split('\n')
        for n in range(len(names)):
            while True:
                rn = randrange(len(working_list) - 1)
                names[n][1] = working_list[rn]
                if names[n][1][-1] == '+' and names[n][3] == 'женский':
                    names[n][1] = names[n][1].rstrip('+');
                    break
                if names[n][1][-1] != '+' and names[n][3] == 'мужской':
                    break
 
    new_names = Path(path[0]) / 'surname.txt'
    with open(new_names, encoding='utf-8') as filein:
        working_list = filein.read()
        working_list = working_list.split('\n')
        for n in range(len(names)):
            while True:
                rn = randrange(len(working_list) - 1)
                names[n][2] = working_list[rn]
                if names[n][2][-1] == '+' and names[n][3] == 'женский':
                    names[n][2] = names[n][2].rstrip('+');
                    break
                if names[n][2][-1] != '+' and names[n][3] == 'мужской':
                    break
                    
    return None
                    
def generate_person() -> dict:
    """Функция которая генерирует анкету человека со случайными данными"""
    new_names = dict()
    name_ = names[randrange(len(names) - 1)]
    new_names['имя'] = name_[0]
    new_names['отчество'] = name_[1]
    new_names['фамилия'] = name_[2]
    new_names['пол'] = name_[3]
    new_names['дата рождения'] = date(1990, 1, 1) + timedelta(randrange(10000))
    gen_int = ''.join(list(str(randrange(9)) for n in range(9)))
    new_names['мобильный'] = ''.join(['+79', gen_int])
                                        
    return new_names
    
# >>> from pprint import pprint
# >>>
# >>> load_data()
# >>>
# >>> pprint(generate_person(), sort_dicts=False)
# {'имя': 'Гриша',
 # 'отчество': 'Михайлович',
 # 'фамилия': 'Пестреков',
 # 'пол': 'мужской',
 # 'дата рождения': datetime.date(2003, 2, 6),
 # 'мобильный': '+79226275231'}
# >>> pprint(generate_person(), sort_dicts=False)
# {'имя': 'Адексей',
 # 'отчество': 'Георгиевич',
 # 'фамилия': 'Пестреков',
 # 'пол': 'мужской',
 # 'дата рождения': datetime.date(2005, 6, 16),
 # 'мобильный': '+79155071234'}
                  
                  
                  
                  
                  
                  
                  
                  
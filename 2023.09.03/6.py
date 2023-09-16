from sys import path
from pathlib import Path
from utils import important_message
import data.vars
import pprint
import random
import time

def main() -> None:
    """Функция для запуска игры в викторина"""
    print(important_message(data.vars.APP_TITLE))
    print(f'\n{data.vars.HELP}\n\n')
    file_quiz = Path(path[0]) / 'data/questions.quiz'
    with open(file_quiz, encoding='utf-8') as filein:
        text_quiz = filein.read()
    text_quiz = text_quiz.split('\n\n')
    text_quiz = random.sample(text_quiz, data.vars.N)

    questions_list = list()
    for quiz in text_quiz:
        quiz = quiz.split('\n')
        questions_list.append(quiz)
    
    scores = 0
    
    for quiz in questions_list:
        print(quiz[0])
        right_answer = 0
        for v in quiz[1:]:
            if '+' in v:
                right_answer = quiz.index(v)
                v = list(v)
                v.remove('+')
                v = ''.join(v)
            print(f'  {v}')
        time_start = time.perf_counter()
        ord_quiz = ord(str(len(quiz)))
        while True:
            user_response = input(f'{data.vars.PROMPT}')
            if 49 <= ord(user_response) <= ord_quiz:
                time_stop = time.perf_counter()
                time_result = round((time_stop - time_start))
                if round(time_stop - time_start) > data.vars.TIMER:
                    if user_response == str(right_answer):
                        scores += data.vars.CORRECT_TIMEOUT
                        print(f'Верно, но недостаточно быстро. ({time_result} c)\n')
                        break
                    else:
                        scores += data.vars.INCORRECT
                        print('Неверно...\n')
                        break
                else:
                    if user_response == str(right_answer):
                        scores += data.vars.CORRECT_TIME
                        print(f'Верно! ({time_result} c)\n')
                        break
                    else:
                        scores += data.vars.INCORRECT
                        print('Неверно...\n')
                        break                
            else:
                print(data.vars.ERR_PREFIX)
    
    print(f'Ваш счет: {scores}')
    
    return None
    
# >>> main()
# #===================================================================================================================#
# #                                                                                                                   #
# #                                            ИСТОРИЧЕСКАЯ БЛИЦ-ВИКТОРИНА                                            #
# #                                                                                                                   #
# #===================================================================================================================#

# Приветствуем в викторине по истории!
# Проверьте своё знание истории России с помощью интересных вопросов.

# Все вопросы имеют варианты ответов, среди них только один верный. За отведённое время (20 с) вам необходимо ввести номер варианта после приглашения для ввода и нажать клавишу Enter.


# Кто в 1964 году основал первый в мире музыкальный театр для детей?
  # 1. Сергей Образцов
  # 2. Юрий Куклачёв
  # 3. Наталья Сац
  # 4. Станиславский и Немирович-Данченко
 # > 3
# Верно, но недостаточно быстро. (32 c)

# В каком российском городе во время Первой русской революции 1905 года был образован первый в России общегородской Совет рабочих депутатов?
  # 1. Москва
  # 2. Рязань
  # 3. Вологда
  # 4. Иваново
 # > 1
# Неверно...

# Какая книга в 1708 году была впервые напечатана новым гражданским шрифтом, введённым Петром I?
  # 1. «Азбука»
  # 2. «Апостол»
  # 3. «Геометрия»
  # 4. «Часовник»
 # > 4
# Неверно...

# На каком языке в 1774 году был издан первый каталог картинной галереи Эрмитаж?
  # 1. На французском
  # 2. На немецком
  # 3. На русском
  # 4. На английском
 # > 1
# Верно! (12 c)

# Что получает россиянин, когда впервые устраивается на работу?
  # 1. Трудовую книжку
  # 2. Трудовое знамя
  # 3. Трудовой орден
  # 4. Трудовую зачётку
 # > 1
# Верно! (4 c)

# Ваш счет: 50

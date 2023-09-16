from shutil import get_terminal_size
import os
from shutil import copy2
from sys import path
from pathlib import Path

def important_message(text: str)-> str:
    """Функция выводит текст в рамке для 2.py"""
    work_text = list(text) # рабочий перечень символов текста для дальнейшего ввода в рамку
    len_text = len(text) # длина вводимого текста
    number_of_columns = os.get_terminal_size().columns - 4 # число столбцов (минус 4 добавлен чтобы рамка помещалась в терминал)
    num_letters = number_of_columns - 6 # количество максимальных букв в строке
    number_of_rows = divmod(len_text, num_letters)[0] + 5 # число строк
    
    result_text = list('#')
    for row in range(number_of_rows):
        for colum in range(number_of_columns):
            if colum == number_of_columns - 1:
                result_text.append('#\n#') 
            elif row == 0 or row == number_of_rows - 1:
                result_text.append('=')
            elif 0 <= colum <= 1 or (number_of_columns - 3) <= colum < (number_of_columns - 1):
                result_text.append(' ')
            elif row == 1 or row == number_of_rows - 2:
                result_text.append(' ')
            elif colum != 0 and colum == 2:
                result_line_text = list()
                for n in range(num_letters):
                    if len(work_text) != 0:
                        result_line_text.append(work_text[0])
                        work_text.pop(0)
                result_text.append(''.join(result_line_text).center(num_letters + 1))
    result_text.pop(-1)
    result_text.append('#')
    return ''.join(result_text)
    
def load_file(file_path: str | Path) -> 'module':
    """Функция выводит текст в рамке для 2.py"""
    result_copy = Path(path[0]) / ('copy_' + file_path.name)
    copy2(file_path, result_copy)
    return result_copy
    
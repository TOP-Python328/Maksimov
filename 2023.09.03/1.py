from pathlib import Path
from sys import path

def list_files(absolute_path: str) -> tuple[str]:
    """Функция которая возвращает кортеж с именами файлов в каталоге по переданному пути"""
    scripts_dir = Path(path[0]) / absolute_path
    try:
        path_list = tuple((path_.name for path_ in scripts_dir.iterdir() if path_.is_file()))
        return path_list
    except:  
        return None
 
# >>> list_files('data') 
# ('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')

# >>> print(list_files('data_2'))
# None
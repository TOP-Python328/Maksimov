from pathlib import Path
from sys import path
from csv import reader, writer

class CountableNouns:
    """класс который предоставляет интерфейс для работы с файловой базой существительных"""
    
    db_path: Path = Path(path[0]) / 'words.csv' # путь к файлу с базой существительных;
    words: dict[str, tuple[str, str]] = {} # соответствие между существительным в единственном числе и кортежем из двух словоформ/слов во множественном числе, согласующихся с числительными "два" и "пять";
    with open(db_path, encoding='utf-8') as filein:
        file_reader = reader(filein, delimiter = ',') 
        words = {line[0]: tuple(line[1:]) for line in file_reader} 
    
    
    @classmethod
    def save_words(cls, word1: str = None) -> None:
        """запрашивает в stdin у пользователя два или три слова согласующихся с числительными, добавляет полученные значения в поле класса words и дописывает их в файл с базой существительных"""

        new_words = ['один', 'два', 'пять']
        template = 'введите слово, согласующееся с числительным "{}": '
        
        if not word1:
            new_words = [input(template.format(nw)) for nw in new_words]  
        else:
            new_words = [input(template.format(nw)) for nw in new_words[1:]]
            new_words.insert(0, word1)
        cls.words[new_words[0]] = tuple(new_words[1:])
        
        with open(cls.db_path, mode="a", encoding='utf-8') as fileout:
            file_writer = writer(fileout, delimiter = ",", lineterminator="\n")
            file_writer.writerow(new_words)

    
    @classmethod
    def pick(cls, number: int, word: str) -> str:
        """принимает в качестве аргументов число и существительное для согласования в единственном числе, возвращает согласованное с переданным числом существительное"""
        
        if not word in cls.words:
            cls.save_words(word)
        
        choice_words = word, *cls.words[word]
        last_digit = number % 10
        decade_digit = number % 100 // 10
        
        if decade_digit == 1 or last_digit > 4:
            return choice_words[2]
        if last_digit == 1:
            return choice_words[0]
        return choice_words[1]
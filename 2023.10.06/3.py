class ChessKing:
    """класс который описывает шахматную фигуру короля"""
    fiels: dict[str, int] = {'abcdefgh'[i-1]: i for i in range(1, 9)} # соответствие между буквой, обозначающей вертикаль шахматной доски, и числом;
    ranks: dict[str, int] = {'12345678'[i-1]: i for i in range(1, 9)} # соответствие между строковым представлением числа, обозначающего горизонталь шахматной доски, и числом;
    
    def __init__(self, in_color: str = 'white', position: str = 'e1'):
        """конструктор класса"""
        self.color = in_color # цвет фигуры;
        if in_color == 'black':
            position = 'e8' 
        self.square = position # поле шахматной доски, на котором в данный момент находится фигура;

        
    def is_turn_valid(self, new_square: str) -> bool:
        """функция проверки возможности для данной фигуры ход с текущего поля на новое"""
        fiels = self.fiels
        ranks = self.ranks
        str_motion = fiels[new_square[0]] - fiels[self.square[0]] # разница длины хода по буквенным координатам;
        int_motion = ranks[new_square[1]] - ranks[self.square[1]] # разница длины хода по численным координатам;
        if new_square[0] not in 'abcdefgh':
            return False
        elif new_square[1] not in '12345678':
            return False
        elif str_motion > 1 or str_motion < (-1):
            return False
        elif int_motion > 1 or int_motion < (-1):
            return False
        else:
            return True
        
    def turn(self, new_square: str) -> ValueError | None:
        """функция принимает на вход строку нового поля и выполняет ход, выбрасывает ValueError в случае невозможности выполнить ход"""
        if self.is_turn_valid(new_square) == False:
            raise ValueError
        else:
            self.square = new_square
            return None
    
    def __str__(self):
        """человекочитаемое строковое представление"""
        return f'{list(globals().keys())[-1].upper()}: {self.square}'
            
        
    def __repr__(self):
        """машиночитаемое строковое представление"""
        return f'{list(globals().keys())[-1].upper()}: {self.square}'
    

# >>> wk = ChessKing()
# >>> wk.color
# 'white'
# >>> wk.square
# 'e1'
# >>>
# >>> wk.turn('e2')
# >>> wk
# WK: e2
# >>>
# >>> wk.turn('e4')
# ...
# ValueError
# >>>
# >>> bk = ChessKing('black')
# >>> print(bk)
# BK: e8
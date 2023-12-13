class Tetrahedron:
    """класс с именем Tetrahedron, который описывает правильный тетраэдр"""
    def __init__(self, edge: float):
        self.edge = edge

    def surface(self)->float:
        # вычисление площади поверхности;
        return (self.edge**2) * (3**(1/2))

    def volume(self)->float:
        # вычисление объёма тела;
        return ((self.edge**3)/12)*(2**(1/2))
    
# >>> t1 = Tetrahedron(5)
# >>> t1.edge
# 5
# >>> t1.surface()
# 43.30127018922193
# >>> t1.volume()
# 14.73139127471974
# >>>
# >>> t1.edge = 6
# >>> t1.surface()
# 62.35382907247958

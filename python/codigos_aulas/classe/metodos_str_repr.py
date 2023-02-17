class Ponto:
    def __init__(self, x) :
        self.x = x
        self.y = x
    
    def __str__(self):
        return f"Classe que define uma coordenada: ({self.x}, {self.y})"
    
    def __repr__(self):
        return f"<Classe {type(self).__name__} em 0x{id(self):>x} Forma: ({self.x},{self.y})>"
    
    @staticmethod
    def soma_ponto(x, y):
        return x + y

    @property 
    def x(self):
        return self._x
    
    @property 
    def y(self):
        return self._y
    
    @x.setter
    def x(self, valor):
        self._x = valor
        self._y = valor + 1
        
    @y.setter
    def y(self, valor):
        self._y = valor
        
    def __add__(self, other):
        return self.x + other.x 
    
    @x.deleter
    def x(self):
        del self._x

p = Ponto(2)

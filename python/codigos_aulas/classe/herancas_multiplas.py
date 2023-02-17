import numpy as np

class Coordenadas:
    def __init__(self, x, y):
        
        if type(x) != np.ndarray or type(y) != np.ndarray:
            raise TypeError("x e y devem ser um np.ndarray")
        
        self.x = np.array(x)
        self.y = np.array(y)
    
    def __str__(self):
        return f"Coordenadas: x = {self.x}, y = {self.y}"
    
    def __repr__(self):
        return f"<Classe {Coordenadas.__name__} em {hex(id(self))}>"
    
    def __add__(self, outro_ponto):
        return np.array([self.x[0] + outro_ponto.x[0], self.x[0] + outro_ponto.x[0]])
     
class DistEuclidian(Coordenadas):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def dist_eucli(self):
        return np.sqrt((self.x ** 2).sum() + (self.y ** 2).sum())
        
p1 = Coordenadas(np.array([1, 2]), np.array([4,5]))       
p2 = Coordenadas(np.array([4, 5]), np.array([1,2]))       



d = DistEuclidian(p1.x, p1.y)
d.dist_eucli()
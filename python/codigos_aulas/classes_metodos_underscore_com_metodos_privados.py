class Classe1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __soma_xy_1(self):
        return self.x + self.y
        
class Classe2(Classe1):
    def __init__(self, Class, z):
        self.x = Class.x
        self.y = Class.y
        self.z = z

    def soma_xy_z(self):
        return super()._Classe1__soma_xy_1() + self.z

p1 = Classe1(3,2)
p2 = Classe2(p1, 3)
p2.soma_xy_z()
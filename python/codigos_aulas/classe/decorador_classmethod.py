class Qualquer:
    x = list()
        
    @classmethod
    def add_valor(cls, valor):
        cls.x.append(valor)

obj_qualquer = Qualquer()
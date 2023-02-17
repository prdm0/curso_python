# Aqui irei usar o operador | que muitas vezes
# usamos como operador de OR lógico. Também irei
# utilizar o conceito de decorador.

# Funções infixas trabalham da seguinte forma:
# arg1 |func| arg2, em que o elemento | poderia ser 
# outros, como +, se tivesse utilizado os métodos
# dunder (métodos mágicos) __add__ e __radd__, 
# por exemplo.

class Infix:
    
    def __init__(self, func):
        self.func = func
        
    def __ror__(self, x):
        return Infix(lambda y: self.func(x, y))
    
    def __or__(self, x):
        return self.func(x)
        
@Infix 
def conta(x, y):
    return x/y + 1    
        
print(f"Resultado: {1 |conta| 2}")

class StrSomaNum:
    def __init__(self, func):
        return self.func = func
    
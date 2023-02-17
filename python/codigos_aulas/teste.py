import functools as fct
import math


l = [1, 6, 7, 10, 2, 8, 4]

def acumular(x, y):
    return math.cos(x) + math.sin(y)

fct.reduce(acumular, x)

def meu_reduce(f, x):
    
    acumulando = f(x[0], x[1])
    
    for i in x[2:]:
        acumulando += f(acumulando, i)
    
    return acumulando
    
meu_reduce(acumular, x)
    
    


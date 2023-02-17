# Tratamento de erro na função filter() que 
# retorna um iterador. 

# Note que a função meu_filtro retorna também um iterador
# porém, mesmo que a sequência iteravel acabe, o iterador
# continuará devolvendo "r", que nesse caso é None.

def meu_filtro(*args, r = None, **kwargs):
    it = filter(*args, **kwargs)
    
    try:
        while True:
            valor = it.__next__()
            yield valor
    except StopIteration:
        while True:
            yield r
            
it = meu_filtro(lambda x: x%2, [1, 2, 3, 4])

list(map(lambda i: it.__next__(), range(6)))
from toolz.curried import *
from toolz import concat
# Computando a frequência:
frequencies([1,-1, 1])
frequencies(['gato', 'cachorro', 'cachorro'])

# Concatenando em uma única lista:
list(toolz.concat([[1], [2,3, [6, 7, 7]]]))
list(toolz.concat([[], [1], [2,6], [7]]))

def iseven(n): return n % 2 == 0

# Complementar de iseven:
isodd = complement(iseven) 

# Usando partial
def soma3(x, y, z):
    return x + y + z

soma1 = toolz.partial(soma3, 1, 2)

# Usando compose:

@curry
def limpando(palavra):
   return palavra.lower().strip(r" ,\\/\'\"@-_~=()%$!?+[]{}")

contando = compose(frequencies, partial(map, limpando), str.split)

merge({'d': 1}, {'a': 3})

import toolz

toolz.concat([[], [1,2, [5]]])


# Com o método curry podemos fazer a aplicação aprcial.
@curry
def soma_dois(x, y, z):
    return x + y + z

soma_z = soma_dois(x = 1, y = 2)
soma_z(z = 4)
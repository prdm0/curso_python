from toolz.curried import *

def e_par(x):
    if x % 2 == 0:
        return True
    else:
        return False
 
lista = [2, 1, 3, 8, 10, 11, 12]  
      
# FORMA I    
d = groupby(e_par, lista)

# FORMA II
d_for = dict({True: [], False: []})
for i in lista:
    if e_par(i):
        d_for[True].append(i)
    else: 
         d_for[False].append(i)
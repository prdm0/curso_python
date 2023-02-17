# O método mro() é útil para especificar as hierarquias de 
# heranças:

class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(C):
    pass

print(D.mro())

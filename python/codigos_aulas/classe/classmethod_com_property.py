class SomaUm:

    valor = 0
        
    @classmethod
    @property
    def soma_um(cls):
        cls.valor += 1
    
# Podemos chamar soma_um como um atributo. 
SomaUm.soma_um
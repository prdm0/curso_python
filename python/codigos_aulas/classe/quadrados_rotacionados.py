import turtle

caneta = turtle.Turtle()

class Quadrado(turtle.Turtle):
    
    def __init__(self, lado = 100, angulo = 0):
        turtle.Turtle.__init__(self)
        self.lado = lado
        self.angulo = angulo
    
    def desenhar(self):
        
        self.right(self.angulo)
    
        def __desenhando_lados(i):
            self.fd(self.lado)
            self.right(90)
            
        list(map(lambda i: __desenhando_lados(i), range(4)))
    
    @property
    def forma(self):
    
        for i in range(36):
            self.desenhar()
            self.left(10)
            
caneta = turtle.Turtle()            
quadrado = Quadrado()
quadrado.pensize(4)
quadrado.forma
turtle.exitonclick()
turtle.bye()
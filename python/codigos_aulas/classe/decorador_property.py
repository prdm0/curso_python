class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        return 2 * self._radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.radius) # 5
c.radius = 10
print(c.radius) # 10
print(c.diameter) # 20
print(c.area) # 78.5

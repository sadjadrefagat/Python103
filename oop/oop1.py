from math import pi


class Circle:
    def __init__(self, r):
        self.radius = r

    def calc_area(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f'Circle with radius = {self.radius}'

    def diameter(self):
        return 2 * self.radius

    def __len__(self):
        return self.diameter()

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __add__(self, r: int):
        return Circle(self.radius + r)
    
    def __eq__(self, other):
        return self.radius == other.radius


c1 = Circle(5)
c2 = Circle(5)
if c1 == c2:
    print('Yes')
else:
    print('No')

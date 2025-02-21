class Circle:
    def __init__(self, r):
        self.radius = r
        
    def __eq__(self, other):
        return self.radius == other.radius
        
c1 = Circle(10)
c2 = Circle(10)

if c1 == c2:
    print("Yes")
else:
    print("No")
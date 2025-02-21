class Circle:
    def __init__(self, r, color):
        self.radius = r
        self.color = color

    def __eq__(self, other):
        return self.radius == other.radius


c1 = Circle(10, "red")
c2 = Circle(10, 'blue')

print(c1)
print(c2)

if isinstance(1, float):
    print("Yes")
else:
    print("NO")

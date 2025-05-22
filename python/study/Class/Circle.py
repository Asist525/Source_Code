class Circle:
    def __init__(self, radius=0):
        self.fie = 3.141592
        self.radius = radius
    def getArea(self):
        return self.fie * self.radius * self.radius
    def getPrimeter(self):
        return 2 * self.fie * self.radius

a = Circle(10)
print(a.getArea())
print(a.getPrimeter())

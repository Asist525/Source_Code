class circle:
    def __init__(self, radius=0):
        self.radius = radius
        self.pie = 3.141592
    def getArgs(self):
        return self.radius * self.radius * self.pie, 2 * self.radius * self.pie
    def setArgs(self, radius):
        self.radius = radius

a = circle(10)
x, y = a.getArgs()
print(f"원의 면적 {x}")
print(f"원의 둘레 {y}")


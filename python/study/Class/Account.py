class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    def __add__(self, other):
        return Vector(self.__x + other.x, self.__y + other.y)
    def __sub__(self, other):
        return Vector(self.__x - other.x, self.__y - other.y)
    def __eq__(self, other):
        return self.__x == other.x and self.__y == other.y
    def __str__(self):
        return (f"{self.__x}, {self.__y}")

a = Vector(0, 1)
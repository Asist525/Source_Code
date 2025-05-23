class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __add__(self, other):
        return Vector(self.__x + other.get_x(), self.__y + other.get_y())

    def __sub__(self, other):
        return Vector(self.__x - other.get_x(), self.__y - other.get_y())

    def __eq__(self, other):
        return self.__x == other.get_x() and self.__y == other.get_y()

    def __str__(self):
        return f"({self.__x}, {self.__y})"

u = Vector(0, 1)
print(u)        # (0, 1)

v = Vector(1, 0)
print(v)        # (1, 0)


a = u + v
print(a)        # (1, 1)

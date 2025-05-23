class test:
    def __init__(self,f):
        self.__radius = f
    def getArgs(self):
        return self.__radius

a = test(10)
print(a.getArgs())
class Car:
    def __init__(self, speed=0, color="blue", model="E-class"):
        self.speed = speed
        self.color = color
        self.model = model
    
    def getArgs(self, speed):
        self.speed = speed
        print(f"자동차의 속도는 {self.speed}")
        
    def show(self): 
        print(f"자동차의 속도는 {self.speed}")
        print(f"자동차의 색상은 {self.color}")
        print(f"자동차의 모델은 {self.model}")
        
        
a = Car()
print("자동차 객체를 생성하였습니다.")
a.show()
a.getArgs(60)

        
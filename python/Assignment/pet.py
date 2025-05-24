from random import randrange

class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    
    def __init__(self, name="KITTY"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        
    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return 'happy'
        elif self.hunger > self.hunger_threshold:
            return 'hungry'
        else:
            return 'bored'
        
    def __str__(self):
        return f'My name is {self.name}.\nI feel {self.mood()} now.'
    
    def cry(self):
        raise NotImplementedError('Subclasses must implement this method')
    
    def feed(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)
    def play(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)
        

class Cat(Pet):
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound # 고양이 소리

    def mood(self):
        if self.hunger > self.hunger_decrement:
            return 'hungry'
        elif self.boredom < 2:
            return 'not bored. Leave me alone'
        elif self.boredom > self.boredom_decrement:
            return 'bored'
        else:
            return 'happy'
            
    def cry(self):
        return self.sound
    
class Dog(Pet):
    def __init__(self,name, sound):
        self.name = name
        self.sound = sound
    def mood(self):
        if self.hunger > self.hunger_decrement and self.boredom > self.boredom_decrement:
            return 'bored and hungry'
        else:
            return 'happy'
        
    def cry(self):
        return self.sound
    
    

def main():
    print("========================cat===================")
    c1 = Cat('Kitty', 'Meow') # 고양이 및 울음소리 매개변수 입력
    c1.boredom = 8 # 클래스 변수 지정
    c1.hunger = 11
    print(c1)
    print('========Feed to Kitty===========')
    c1.feed()
    print(c1)
    print('========Play with kitty===========')
    c1.play()
    print(c1, c1.cry())
    print('========play with Kitty===========')   
    c1.play()
    print(c1)
    

    print("========================Dog===================")
    d1 = Dog('Moe', 'Woof!') # 고양이 및 울음소리 매개변수 입력
    d1.boredom = 8 # 클래스 변수 지정
    d1.hunger = 11
    print(d1)
    print('========Feed to Moe===========')
    d1.feed()
    print(d1)
    print('========Play with Moe===========')
    d1.play()
    print(d1, d1.cry())
    print('========play with Moe===========')   
    d1.play()
    print(d1, d1.cry(), d1.cry())

if __name__ == "__main__":
    main()
class Person:
    def __init__(self, age, name):
        self.name = name
        self.age = age
    def __repr__(self):
        return f'[<이름: {self.name}>, <나이: {self.age}>]'

Person_list = [Person(20, "홍길동"), Person(35, "김철수"), Person(38, "최지영")]

print(Person_list) # 기본 리스트
print(sorted(Person_list, key=lambda p:p.age, reverse=True)) # age순 내림차순 리스트

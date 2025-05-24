class MyCounter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
        
    def __iter__(self): # 자기 자신 반환
        return self
    
    def __next__(self):
        if self.current > self.high:
            raise StopIteration # 반복을 끝내기 위한 장치
        else:
            self.current += 1 # self.current에 저장하기 위한 += 1
            return self.current -1 # 1을 먼저 더했으므로, 리턴값에서 1을 빼줘야한다.

c = MyCounter(1, 10)
for i in c:
    print(i, end=" ")
print()
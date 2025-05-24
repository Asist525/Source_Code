def fibonachil_for_function(x):
    if x==0:
        return 0
    if x==1:
        return 1
    if x>1:
        a, b = 0, 1
        for _ in range(2, x+1):
            a, b = b, a+b
        return b
def fibonachi_for_requarsive(x):
    if x==0:
        return 0
    if x==1:
        return 1
    if x>1:
        return fibonachi_for_requarsive(x-1) + fibonachi_for_requarsive(x-2)


class fibo:
    def __init__(self, high=10):
        self.a = 0
        self.b = 1
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        n = self.a + self.b
        if n > self.high:
            raise StopIteration()
        
        self.a = self.b
        self.b = n
        return n

def main():
    x = 10
    print(f"{fibonachi_for_requarsive(x)}")
    print(f"{fibonachil_for_function(x)}")
    for i in fibo():
        print(i, end = " ")
if __name__=="__main__":
    main()
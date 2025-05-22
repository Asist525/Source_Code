class Account:
    def __init__(self,balance=100):
        self.__balance = balance
    
    def withdrow(self, withdrow):
        self.__balance = self.__balance - withdrow
        print(f"통장에서 {withdrow}가 출금되었음")
    def despoit(self, despoit):
        self.__balance = self.__balance + despoit
        print(f"통장에 {despoit}가 입금되었음")
        
    def now(self):
        print(self.__balance)
    
money = Account()
money.withdrow(100)
money.despoit(10)
money.now()
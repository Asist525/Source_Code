class Account:
    def __init__(self, balance=100):
        self.__balance = balance
    def withdrow(self, balance):
        print(f"통장에서 {balance}가 출금되었음")
        return self.__balance - balance
    def despoit(self, balance):
        print(f"통장에 {balance}가 입금되었음")
        return self.__balance + balance

money = Account()
money.withdrow(100)
money.despoit(10)
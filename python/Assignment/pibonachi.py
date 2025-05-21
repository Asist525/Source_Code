def fibo_recursive(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibo_recursive(n-1) + fibo_recursive(n-2)


def main():
    n = int(input("n: "))
    res_list = fibo_recursive(n)
    
    if res_list is not None:
        print(res_list)
    else:
        print("Wrong Input")
    
if __name__ == "__main__":
    main()
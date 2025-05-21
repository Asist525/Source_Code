def main():
    num = int(input("숫자를 입력하시오: "))
    
    num_list = []
    while(num % 10):
        num_list.append(num % 10)
        num = num // 10   
        
    num_list = [x for x in num_list[::-1]]
    print(num_list)
    
    

if  __name__ == "__main__":
    main()
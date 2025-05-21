def find_divosor_list(n):
    divosor_list = []
    
    for i in range(1, n+1):
        if n % i == 0:
            divosor_list.append(i)
            
    return divosor_list


def main():
    n = int(input("n: "))
    res_list = find_divosor_list(n)
    print(res_list)
    
if __name__ == "__main__":
    main()
def my_upper(*text): # 이 경우  text는 list형식이다.
    results = []
    for i in text:
        
        if isinstance(i, str): # 문자인 경우
            for j in i: 
                if 'a' <=  j <= 'z':
                    results.append(chr(ord(j) - 32))
                
                else:
                    results.append(j)
        else: #문자가 아닌 [1,2,3]을 대비
            for j in str(i): # [1,2,3]자체를 문자열로 바꿔서 리스트에 삽입
                results.append(j)
    
    result = ''.join(results)
    return result
        
    

def main():
    
    print(chr(ord('a')-32))

    print(my_upper('These are examples of my_upper()'))
    print(my_upper('my_upper() takes *args of strings and return a list of that turn into upper cases'))
    # 위는 각 한개의 인수, 해당 줄에서 4개의 인수를 받아야 하므로 함수에서 가변 인자 매개변수 처리가 필요하다.
    # 또한 마지막 인수의 경우 문자열이 아니므로 아닌경우의 처리 장치가 필요하다.
    print(my_upper('aaa', 'Bb', 'CCcccC', [1, 2, 3])) 

main()
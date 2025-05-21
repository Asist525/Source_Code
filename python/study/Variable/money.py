money = int(input("물건값을 입력하세요: "))
m_1000 = int(input("1000원 지폐계수"))
m_500 = int(input("500원 동전계수"))
m_100 = int(input("100원 동전계수"))

num = (1000 * m_1000 + 500 * m_500 + 100 * m_100) - money

l_500 = 0
l_100 = 0
l_10 = 0
l_1 = 0

if num // 500 > 0:
    l_500 = num // 500
    num = num - l_500 * 500

if num // 100 > 0:
    l_100 = num // 100
    num = num - l_100 * 100
    
if num // 10 > 0:
    l_10 = num // 10
    num = num - l_10 * 10
    
if num // 1 > 0:
    l_1 = num // 1
    num = num - l_1 * 1

print(f"500원={l_500}, 100원={l_100}, 10원={l_10}, 1원={l_1}")
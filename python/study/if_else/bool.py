a = int(input())
b = int(input())
if a > b:
    print(a)

else:
    print(b)
    

max = a > b

if max == True:
    print(a)
else:
    print(b)
    
print(a if a>b else b)
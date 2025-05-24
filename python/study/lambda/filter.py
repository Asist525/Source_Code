list_a = [1,2,3,4,5,6]
f = lambda x: x%2==0
result = filter(f, list_a)
print(list(result))
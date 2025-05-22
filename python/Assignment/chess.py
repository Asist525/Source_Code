s = input("Your input: ")

if not s:
    x, y = -99, -99

else:
    x = ord(s[0]) - 32 - 65 if ord(s[0])>96 else ord(s[0]) - 65
    y = s[1]

chess_list = [[[1] for x in range(8)] for _ in range(8)]

moving = [[2,1], [2, -1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [1, -2], [-1, -2]]
bool_list = []
count = 0

for i in range(8):
    if 0<=int(x)<=7 and 0<=int(y)<=7:
        if 0 < int(x) -  moving[i][0] < 8 and 0 < (int(y) - int(moving[i][1])) < 8:
            bool_list.append(i)
            count += 1

if count == 0:
    print("Wrong corrdinante")
    print("-1")
else:
    print(count)




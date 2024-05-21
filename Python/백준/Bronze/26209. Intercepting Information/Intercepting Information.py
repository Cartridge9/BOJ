a = list(map(int, input().split()))
s = 1
for i in a:
    if i <= 1:
        pass
    elif i == 9:
        s-=1
        print("F")
        break
if s == 1:
    print("S")
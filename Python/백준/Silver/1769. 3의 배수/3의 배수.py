a = input()
cnt = 0
if int(a) < 10:
    pass
else:
    while 1:
        a = str(a)
        a = list(map(int, a))
        a = sum(a)
        if a // 10 < 1:
            cnt+=1
            break
        else:
            cnt+=1
print(cnt)
a = int(a)
if a == 3 or a == 6 or a == 9:
    print("YES")
else:
    print("NO")
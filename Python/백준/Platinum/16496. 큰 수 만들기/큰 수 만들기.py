n = int(input())
li = []
a = list(map(int, input().split()))
if sum(a)==0:
    print(0)
else:
    for i in a:
        s = str(i)
        l = len(s)
        while len(s) < 10:
            s+=s[len(s)-l]
        li.append([s,i])
    li.sort(key=lambda x:x[0], reverse=True)

    for j in range(n):
        print(li[j][-1],end="")
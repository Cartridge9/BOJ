n, m = map(int, input().split())
x = list(map(int, input().split()))
l = []
x.sort()
for i in range(len(x)):
    for j in range(len(x)):
        for h in range(len(x)):
            if x[i] != x[j] and x[i] != x[h] and x[j] != x[h]:
                l.append(x[i]+ x[j]+ x[h])
l.append(m)
l.sort()
if l.count(m) >= 2:
    print(l[l.index(m)])
else:
    print(l[l.index(m)-1])
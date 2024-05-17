n = int(input())
x = []
f = [[]]
cnt = 1
for i in range(n):
    x.append(input())
x.sort(key=len)
for i in range(len(x)):
    if len(x[i]) == cnt:
        f[-1].append(x[i])
    elif len(x[i]) > cnt:
        cnt=len(x[i])
        f.append([])
        f[-1].append(x[i])
for i in range(len(f)):
    f[i] = set(f[i])
    f[i] = list(f[i])
    f[i].sort()
for i in range(len(f)):
    for j in range(len(f[i])):
        print(f[i][j])

n, m = map(int, input().split())
x = []
for i in range(n):
    x.append([0])
for i in range(m):
    a, b, c = map(int, input().split())
    for j in range(a-1, b):
        for h in range(len(x[j])):
            x[j].pop()
        x[j].append(c)
for i in range(n):
    print(x[i][0], end=" ")
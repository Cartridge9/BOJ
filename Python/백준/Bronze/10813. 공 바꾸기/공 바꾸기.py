n, m = map(int, input().split())
x = []
for i in range(n):
    x.append(i+1)
for i in range(m):
    a, b = map(int, input().split())
    x[a-1], x[b-1] = x[b-1], x[a-1]
for i in range(n):
    print(x[i], end=" ")
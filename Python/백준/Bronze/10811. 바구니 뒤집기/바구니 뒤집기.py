n, m = map(int, input().split())
x = list(range(1, n+1))
c = 0
for i in range(m):
    a, b = map(int, input().split())
    c = x[a-1:b]
    c.reverse()
    x[a-1:b] = c
for i in range(n):
    print(x[i], end=" ")
l = []
c = 0
for i in range(100):
    l.append([])
    for j in range(100):
        l[i].append(0)
n = int(input())
for h in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            l[99-y-j][x+i] = 1
# for i in range(100):
#     for h in range(100):
#         print(l[i][h], end=" ")
#     print()
for i in range(100):
    c += l[i].count(1)
print(c)
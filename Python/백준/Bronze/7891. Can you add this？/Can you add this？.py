n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
for i in range(n):
    print(sum(l[i]))
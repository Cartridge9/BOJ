pi = 1, 1, 2, 2, 2, 8
x = []
n = list(map(int, input().split()))
for i in range(6):
    x.append(pi[i] - n[i])
for i in range(6):
    print(x[i], end=" ")
x  = list(range(1, 31))
for i in range(28):
    n = int(input())
    x[n-1] = 0
for i in range(len(x)):
    if x[i] == 0:
        continue
    else:
        print(x[i])
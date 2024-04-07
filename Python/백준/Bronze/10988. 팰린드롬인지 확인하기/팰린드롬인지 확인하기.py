n = list(input())
bn = n
x = 0
for i in range(len(n)):
    if n[-(i+1)] == bn[i]:
        x += 1
if x == len(n):
    print(1)
else: print(0)
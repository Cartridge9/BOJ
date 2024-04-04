n = int(input())
x = list(map(int, input().split()))
xm = max(x)
for i in range(n):
    x[i] = (x[i]/xm)*100
print(sum(x)/len(x))
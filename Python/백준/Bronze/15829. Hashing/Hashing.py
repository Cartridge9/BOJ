n = int(input())
a = list(input())
x = 0
for i in range(n):
    x+=(ord(a[i])-96)*(31**i)
print(x%1234567891)
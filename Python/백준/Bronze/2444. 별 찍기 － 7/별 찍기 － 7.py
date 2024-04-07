n = int(input())
b = " "
s = "*"
for i in range(2*n-1):
    if i <= n-1:
        print(b*(-(i+1-n))+s*((1)+(i*2)))
    elif i > n-1:
        print(b*(i+1-n)+s*(n*2-i-2)+s+s*(n*2-i-2))
n = int(input())
hs = 0
bl = 0
for i in range(1, n+1):
    hs = "*"*i
    bl = " "*(n-i)
    print(bl+hs)
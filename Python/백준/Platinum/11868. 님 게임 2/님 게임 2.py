n = int(input())
a = list(map(int, input().split()))
b = a[0]
for i in range(1, len(a)):
    b^=a[i]
if b == 0:
    print("cubelover")
else:
    print("koosaga")
    
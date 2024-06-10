n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    a.sort()
    a.pop(0)
    a.pop(-1)
    if a[-1] - a[0] >= 4:
        print("KIN") 
    else:
        print(sum(a))
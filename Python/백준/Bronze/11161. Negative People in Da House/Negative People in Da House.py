for i in range(int(input())):
    c = 0
    min1 = 0
    for j in range(int(input())):
        a, b = map(int, input().split())
        c = c + a - b
        min1 = min(min1, c)
    print(-min1)
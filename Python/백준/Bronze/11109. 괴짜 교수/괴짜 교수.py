for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a+b*d > b*c:
        print("do not parallelize")
    elif a+b*d == b*c:
        print("does not matter")
    else:
        print("parallelize")
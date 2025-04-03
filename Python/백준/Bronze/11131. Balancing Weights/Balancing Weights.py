for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = sum(a)
    if a == 0:
        print("Equilibrium")
    elif a < 0:
        print("Left")
    elif a > 0 :
        print("Right")
n = int(input())
a = sum(list(map(int, input().split())))
if a == 0:
    print("Stay")
elif a > 0:
    print("Right")
elif a < 0:
    print("Left")
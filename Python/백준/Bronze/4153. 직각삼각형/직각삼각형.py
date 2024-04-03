x = []
while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        x.append("right")
    else:
        x.append("wrong")
for i in range(len(x)):
    print(x[i])
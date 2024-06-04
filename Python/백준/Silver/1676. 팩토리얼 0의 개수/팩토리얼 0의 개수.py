import math
n = int(input())
n = list(reversed(list(str(math.factorial(n)))))
x = 0
for i in n:
    if i == "0":
        x += 1
        pass
    else:
        print(x)
        break
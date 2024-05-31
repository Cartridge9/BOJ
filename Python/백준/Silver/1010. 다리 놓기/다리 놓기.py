import math as ma
for i in range(int(input())):
    n, m = map(int, input().split())
    print(ma.factorial(m) // (ma.factorial(n) * ma.factorial(m - n)))
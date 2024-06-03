import math
import copy
import sys
def findn(m):
    if m == 0 or m == 1:
        return 1
    low = 0
    high = 1
    while math.factorial(high) < m:
        high *= 2

    while low <= high:
        mid = (low+high)//2
        midf = math.factorial(mid)
        if midf == m:
            return mid
        elif midf > m:
            high = mid - 1
        elif midf < m:
            low = mid + 1
    return None

m = int(sys.stdin.readline())
print(findn(m))
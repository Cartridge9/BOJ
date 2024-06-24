import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))

total = 0
for a in A:
    if a < 4:
        total ^= 0
    elif 4 <= a <= 15:
        total ^= 1
    elif 16 <= a <= 81:
        total ^= 2
    elif 82 <= a <= 6723:
        total ^= 0
    elif 6724 <= a <= 50625:
        total ^= 3
    elif 50626 <= a <= 2562991875:
        total ^= 1
    else:
        total ^= 2
if total == 0:
    print('cubelover')
else:
    print('koosaga')
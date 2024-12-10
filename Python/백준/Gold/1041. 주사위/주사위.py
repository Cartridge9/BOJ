import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
output = 0

if n == 1:
    print(sum(a) - max(a))
    exit()

s1 = (n - 2) ** 2 * 5 + 4 * (n - 2)
s2 = (n - 2) * 8 + 4
s3 = 4
output += min(a) * s1
k = 100
for i in range(6):
    for j in range(i + 1, 6):
        if i + j == 5:
            continue
        k = min(k, a[i] + a[j])
output += k * s2
k = 150
for i in range(6):
    for j in range(i + 1, 6):
        if i + j == 5:
            continue
        for l in range(j + 1, 6):
            if i + l == 5 or j + l == 5:
                continue
            k = min(k, a[i] + a[j] + a[l])
output += k * s3

print(output)
import sys as s
n = int(s.stdin.readline().rstrip())
c = [0]*10001
for i in range(n):
    num = int(s.stdin.readline().rstrip())
    c[num] += 1
for i in range(10001):
    if c[i] > 0:
        for j in range(c[i]):
            s.stdout.write(f"{i}\n")
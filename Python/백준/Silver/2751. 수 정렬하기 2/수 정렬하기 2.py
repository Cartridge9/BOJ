import sys as s
n = int(s.stdin.readline())
l = [0]*n
for i in range(n):
    l[i] = int(s.stdin.readline())
l.sort()
for i in range(n):
    print(l[i])
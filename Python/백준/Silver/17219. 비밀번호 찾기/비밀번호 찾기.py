import sys
dic = {}
a, b = map(int, input().split())
for i in range(a):
    s = sys.stdin.readline().split()
    dic[s[0]] = s[1]
for i in range(b):
    n = sys.stdin.readline()
    print(dic[n[:-1]])
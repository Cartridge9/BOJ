import sys
input = sys.stdin.readline
m, n = map(int, input().split())
pl = {}
pl2 = {}
for i in range(m):
  a = input().rstrip()
  pl[i+1] = a
  pl2[a] = i+1
  
for j in range(n):
  b = input().rstrip()
  if b.isdigit() == True:
    print(pl[int(b)])
  else:
    print(pl2[b])
import sys
n, x = map(int, sys.stdin.readline().split())
pl = []
cnt = 0
for i in range(n):
  pl.append(int(sys.stdin.readline()))

for i in range(n-1, -1, -1):
   cnt += x // pl[i]
#    print('step',i,"=",pl[i],)
   if x // pl[i] != 0:
    x = x % pl[i]

print(cnt)
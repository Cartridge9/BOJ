import sys
input = sys.stdin.readline
s= set()
n = int(input())
for i in range(n):
  a = input().split()
  if len(a) > 1:
    a[1] = int(a[1])
  if a[0] == 'add' and a[1] not in s:
    s.add(a[1])
  elif a[0] == 'remove' and a[1] in s:
    s.remove(a[1])
  elif a[0] == 'check':
    if a[1] in s: print(1)
    else: print(0)
  elif a[0] == 'toggle':
    if a[1] in s: s.remove(a[1])
    else : s.add(a[1])
  elif a[0] == 'all':
    s = set([i for i in range(1, 21)])
  elif a[0] == 'empty':
    s = set()
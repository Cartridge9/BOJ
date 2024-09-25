n = int(input())
li = [None]*n
top = -1
for i in range(n):
  a = input().split()
  if a[0] == 'push':
    top+=1
    li[top] = a[1]
  elif a[0] == 'pop':
    if top != -1:
      top-=1
      print(li[top+1])
      li[top+1] = None
    else: print(-1)
  elif a[0] == 'size':
    print(top+1)
  elif a[0] == 'empty':
    if top == -1:
      print(1)
    else:print(0)
  elif a[0] == 'top':
    if top != -1:
      print(li[top])
    else:
      print(-1)
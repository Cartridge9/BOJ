st = [None]*50000
top = -1
cnt = []
def push(e):
  global top
  top += 1
  st[top] = e

def pop():
  global top
  top -= 1
  st[top+1] = None

def isEmpty():
  global top
  return top == -1

def show():
  global top
  top = -1
  a = input()
  for ch in a:
    if ch == '(':
      push(ch)
    else:
      if isEmpty():
        return 'NO'
      else:
        pop()
  if not isEmpty(): return 'NO'
  else: return 'YES'

for i in range(int(input())):
  cnt.append(show())
for i in cnt:
  print(i)
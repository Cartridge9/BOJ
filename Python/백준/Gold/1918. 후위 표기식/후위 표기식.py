def prece(op):
  if op == '(' or op ==')' : return 0
  elif op == '+' or op == '-' : return 1
  elif op == '*' or op == '/' : return 2
  else : return -1

def push(e):
  global top
  top += 1
  s[top] = e

def pop():
  global top
  top-=1
  return s[top+1]

def peek():
  global top
  return s[top]

def postfix(expr):
  output = []

  for t in expr:
    if t in '(' : push('(')

    elif t in ')':
      while not top == -1 :
        op = pop()
        if op == '(':
          s[top+1] = None
          break
        else:
          output.append(op)
          s[top+1] = None
    
    elif t in '+-*/':
      while not top==-1:
        op = peek()
        if prece(t) <= prece(op):
          output.append(op)
          pop()
          s[top+1] = None
        else: break
      push(t)
    
    else: output.append(t)

  while not top == -1:
    output.append(pop())
    s[top+1] = None
  return output

top = -1
s = [None]*100

print(*postfix(input()), sep='')
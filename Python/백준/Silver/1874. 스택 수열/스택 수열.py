n = int(input())

group = []

result = []

poplist = []

for i in range(n):
  group.append(int(input()))

class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0
  
  def push(self, item):
    self.items.append(item)
  
  def pop(self):
    if not self.is_empty(): 
      return self.items.pop()
    else:
      return None
  
  def size(self):
    return len(self.items)

stack = Stack()

cnt = 0
for i in range(1, n+1): # 1 2 3 4 5 6 7 8
  # print('step', i)
  if stack.is_empty():
    stack.push(i)
    result.append('+')
    # print('its empty and push', i)
    if group[cnt] == i:
      pass
    elif i == 1:
      continue

  if group[cnt] > stack.items[-1]:
    if stack.items[-1] == i:
      pass
    else:
      stack.push(i)
      # print("+", i)
      result.append('+')
  elif group[cnt] < stack.items[-1]:
    print('NO')
    exit()

  while group[cnt] == stack.items[-1]:
      popItem = stack.pop()
      poplist.append(popItem)
      result.append('-')
      # print('pop',popItem)
      # print(poplist)
      # print(result)
      cnt+=1
      if stack.is_empty():
        break
      if cnt > n:
        break
      elif group[cnt] < stack.items[-1]:
        print('NO')
        exit()
  
  if cnt >= n:
    break
        

if poplist == group:  
  for i in result:
    print(i)

# print(stack.items)
# print('만들 배열:',group)
# print('만든 배열:',poplist)
# print("결과:", result)
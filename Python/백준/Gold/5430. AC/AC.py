import sys
input = sys.stdin.readline
a = []
for i in range(int(input())):
  f = list(input())
  del f[-1]
  m = int(input())
  test = input()

  if test != "[]\n":
    test = list(map(int, test[1:-2].split(',')))
  else:
    test = []

  r = 0
  d = 0
  err = 0
  for i in range(len(f)):
    if f[i] == 'D' and len(test) <= d:
      print('error')
      err += 1
      # a.append('error')
      break

    if f[i] == 'R':
      if r % 2 == 0 and d > 0:
        del test[0:d]
        d = 0
      elif r % 2 == 1 and d > 0:
        del test[-1:-d-1:-1]
        d = 0
      r += 1
    elif f[i] == 'D':
      d+=1
      if i+1 == len(f):
        if r % 2 == 0 and d > 0:
          del test[0:d]
        elif r % 2 == 1 and d > 0:
          del test[-1:-d-1:-1]
    # print(test)
  
  if err != 1:
    if len(test) == 0:
      print('[]')
    else:
      if r % 2 == 1:
        print(str(list(reversed(test))).replace(' ', ''))
      else:
        print(str(test).replace(' ', ''))
  else:
    continue

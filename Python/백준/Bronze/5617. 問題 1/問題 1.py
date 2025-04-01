a = 0 # 예각
b = 0 # 둔각
c = 0 # 직각
isBreak = 0

while(True):
  inpu = list(map(int, input().split()))
  m = max(inpu)
  del inpu[inpu.index(m)]

  if m >= inpu[0]+inpu[1]:
    break

  if m**2 > inpu[0]**2 + inpu[1]**2:
    b+=1
  elif m**2 < inpu[0]**2 + inpu[1]**2:
    a+=1
  elif m**2 == inpu[0]**2 + inpu[1]**2:
    c+=1

print(a+b+c, c, a, b, sep='\n')
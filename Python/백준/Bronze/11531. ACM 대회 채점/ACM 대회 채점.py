d = dict()
count = 0
c = 0
li = []
while(True):
  a = list(map(str, input().split()))
  if a[0] == "-1":
    break
  else:
    t = a[0]
    p = a[1]
    s = a[2]
  
  if p not in d:
    d[p] = [t, s, 0]

  if s != d[p][1]:
    d[p][1] = s 

  if t != d[p][0]:
    d[p][0] = t

  if d[p][1] != "right":
    d[p][2] += 1
  
  if d[p][1] == "right":
    c += int(d[p][0])+int(d[p][2])*20
    count+=1
  
print(count, c)
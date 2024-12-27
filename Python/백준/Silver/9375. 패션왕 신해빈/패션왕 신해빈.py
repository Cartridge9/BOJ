n = int(input())
output = []
for i in range(n):
  m = int(input())
  cl = dict()
  cnt = 0
  for j in range(m):
    name, type = input().split()
    if type not in cl:
      cl[type] = [name]
    else:
      cl[type].append(name)
    # cnt += 1

  # if len(cl) != 1:
  mult = 0
  for h in cl:
    if mult == 0:
      mult += len(cl[h])+1
    else:
      mult *= len(cl[h])+1
  
  if mult == 0:
    output.append(0)  
  else:
    output.append(mult-1)

for i in range(n):
  print(output[i])

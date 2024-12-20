l = dict()
for i in range(int(input())):
  a = input()
  if a in l: l[a] += 1
  else: l[a] = 1

lsort = sorted(l.items(), key=lambda x: x[0])
# print(lsort)
max = ''
maxint = 0
for i in lsort:
  if i[1] > maxint:
    max = i[0]
    maxint = i[1]
print(max)
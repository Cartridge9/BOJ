l = []
for i in range(8):
  a = input()
  l.append(list(a))
c = 0
for i in range(8):
  for j in range(8):
    if i % 2 == 0 and j % 2 == 0 and l[i][j] == "F":
      c += 1
    if i % 2 == 1 and j % 2 == 1 and l[i][j] == "F":
      c += 1
print(c)
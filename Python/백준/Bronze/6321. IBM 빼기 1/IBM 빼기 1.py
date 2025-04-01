n = int(input())
for i in range(n):
  a = list(input())
  for j in range(len(a)):
    if a[j] == "Z":
      a[j] = "A"
      continue
    a[j] = chr(ord(a[j])+1)
  print("String #"+str(i+1))
  print(''.join(a))
  if i != n-1:
    print()

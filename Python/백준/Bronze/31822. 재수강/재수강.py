a = input()
c = 0
n = int(input())
for i in range(n):
  b = input()
  if b[:5] == a[:5]:
    c+=1
  else:
    continue
print(c)
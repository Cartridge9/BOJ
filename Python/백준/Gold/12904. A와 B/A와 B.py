s = list(input())
t = list(input())

for i in range(len(t)):
  if t == s:
    print(1)
    exit()
  if t[-1] == 'A':
    del t[-1]
  else:
    del t[-1]
    t = list(reversed(t))

print(0)
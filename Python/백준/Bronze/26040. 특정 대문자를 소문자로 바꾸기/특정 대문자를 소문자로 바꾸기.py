a = list(input())
x = input().split()

for i in range(len(a)):
  if a[i] in x:
    a[i] = a[i].lower()

print(''.join(a))
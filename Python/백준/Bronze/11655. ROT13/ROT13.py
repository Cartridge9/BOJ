a = list(input())

for i in range(len(a)):
  if 97 <= ord(a[i]) and 122 >= ord(a[i]):
    if (ord(a[i])+13)%122 == 0:
      a[i] = chr((ord(a[i])+13)%122+122)
    elif 1 <= (ord(a[i])+13)%122 < 97:
      a[i] = chr((ord(a[i])+13)%122+96)
    else:
      a[i] = chr((ord(a[i])+13)%122)
  elif 90 >= ord(a[i]) >= 65:
    if 1 <= (ord(a[i])+13)%90 < 65:
      a[i] = chr((ord(a[i])+13)%90+64)
    elif (ord(a[i])+13)%90 == 0:
      a[i] = chr((ord(a[i])+13)%90+90)
    else:
      a[i] = chr((ord(a[i])+13)%90)
print(''.join(a))

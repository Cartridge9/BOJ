n = input()
if n[0:2] == "0x":
  print(int(n, 16))
elif n[0] != "0":
  print(int(n))
else:
  n = "0o" + n[1::]
  print(int(n, 8))
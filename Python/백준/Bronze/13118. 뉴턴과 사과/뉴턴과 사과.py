a = list(map(int, input().split()))
b = list(map(int, input().split()))
try:
  print(a.index(b[0])+1)
except:
  print(0)
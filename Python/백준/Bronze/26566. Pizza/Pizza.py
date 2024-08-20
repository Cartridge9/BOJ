n = int(input())
for i in range(n):
  slice, p = map(int, input().split())
  whole, p2 = map(int, input().split())
  if slice/p < (whole**2*3)/p2:
    print('Whole pizza')
  else:
    print('Slice of pizza')
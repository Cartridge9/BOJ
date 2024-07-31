n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
  k-=a[i]
  if k < 0:
    print(i+1)
    break
else:
    for j in range(n-1, -1, -1):
       k-=a[j]
       if k < 0:
        print(j+1)
        break
    
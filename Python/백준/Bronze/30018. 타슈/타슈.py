n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
for i in range(n):
  if a[i] < b[i]:
    cnt+=(b[i] - a[i])

print(cnt)
n = int(input())
a = list(map(int, input().split()))
# d = {i+1 : a[i] for i in range(len(a))}
# print(d)
# d= sorted(d.items(),key=lambda x: x[1])
# print(d)
a = sorted(a)
# print(a)
cnt = 0
for i in range(n):
  cnt+=sum(a[0:i+1])
print(cnt)
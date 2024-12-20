# a = [2,1,3,1]
# p = [2, 0, 3,1]
# b = [0,0,0,0]
# for i in range(len(a)):
#   print(i)
#   b[p[i]] = a[i]
# print(b)

n = int(input())
a = list(map(int, input().split()))
result = []
asort = list(sorted(a))
for i in range(len(a)):
  result.append(asort.index(a[i]))
  asort[asort.index(a[i])] = -1
# print(a)
# print(asort)
print(*result)

import sys
input = sys.stdin.readline

li = []
n = int(input())
for i in range(n):
  li.append(list(map(int, input().split())))

rank = []

for j in range(n):
  count = 1
  for h in range(n):
    if li[j][0] < li[h][0] and li[j][1] < li[h][1]:
      count += 1
  rank.append(count)
print(*rank)
  
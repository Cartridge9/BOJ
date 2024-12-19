import sys
n, m = map(int, sys.stdin.readline().split())
arr = [[0 * s  for s in range(m)] * v for v in range(n)]

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))

result = []
# print(arr)
for k in range(int(input())):
    i,j,x,y = map(int, sys.stdin.readline().split())
    i-=1
    j-=1
    x-=1
    y-=1
    # print(i,j,x,y)
    cnt = 0
    for h in range(i, x+1):
        # print(h)
        cnt += sum(arr[h][j:y+1])
        # print(sum(arr[h][j:y+1]))
    result.append(cnt)
    # print(result)
for i in result:
    print(i)
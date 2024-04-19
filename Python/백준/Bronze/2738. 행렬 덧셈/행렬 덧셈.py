n, m = map(int, input().split())
x = []
x2 = []
for j in range(n):
	x.append(list(map(int, input().split())))
for h in range(n):
	x2.append(list(map(int, input().split())))
for i in range(n):
	for j in range(m):
		x[i][j] += x2[i][j]
for i in range(n):
	for j in range(m):
		print(x[i][j], end=" ")
	print()
n, m = map(int, input().split())
meml = []
for i in range(n):
    meml.append(int(input()))
for j in range(1, m+1):
	for i in range(1, n):
		if meml[i-1] % j > meml[i] % j:
			meml[i-1], meml[i] = meml[i], meml[i-1]
		else:
			pass
for i in range(n):
	print(meml[i])
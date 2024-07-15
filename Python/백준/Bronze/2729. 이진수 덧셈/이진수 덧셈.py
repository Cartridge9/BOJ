n = int(input())
li = []
for i in range(n):
	a, b = map(str, input().split())
	a = '0b' + a
	b = '0b' + b
	li.append(int(a, 2)+int(b, 2))
	print(format(li[i], 'b'))
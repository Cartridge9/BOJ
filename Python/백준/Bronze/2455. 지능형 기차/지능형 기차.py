li = []
for i in range(4):
	li.append(list(map(int, input().split())))
s = 0
m = 0
for i in range(4):
	s+=li[i][1]
	s-=li[i][0]
	if m > s:
		pass
	else:
		m = s
print(m)
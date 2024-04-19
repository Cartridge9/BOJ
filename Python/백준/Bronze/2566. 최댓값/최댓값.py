x = []
m = []
for i in range(9):
    x.append(list(map(int, input().split())))
for i in range(9):
    m.append(max(x[i]))
print(max(m))
mdex = m.index(max(m))+1
x = x[mdex-1]
xdex = x.index(max(m))+1
print(f"{mdex} {xdex}")
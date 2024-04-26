l = []
for i in range(5):
    l.append(list(map(str, input().split())))
x = ""
for j in range(15):
    for i in range(5):
        if j >= len(l[i][0]) :
            continue
        else:
            x += l[i][0][j]
print(x)
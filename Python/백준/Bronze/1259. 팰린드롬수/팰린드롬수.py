x = []
b = 0
while True:
    a = input()
    if int(a) == 0:
        break
    for i in range(len(a)//2):
        if a[i] != a[-1*(i+1)]:
            x.append("no")
            break
        else:
            b += 1
    if b == len(a)//2:
        x.append("yes")
    b = 0
for i in range(len(x)):
    print(x[i])
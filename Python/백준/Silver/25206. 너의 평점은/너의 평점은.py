gp = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
x = []
x2 = []
for i in range(20):
    g = list(input().split())
    g = g[1:3]
    if g[1] == "P":
        continue
    g[1] = gp[g[1]]
    g[0] = float(g[0])
    x.append(g[0]*g[1])
    x2.append(g[0])
print(f"{sum(x)/sum(x2):.6f}")
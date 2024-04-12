n = input()
x = 0
for i in range(len(n)):
    if "c=" in n:
        x += n.count("c=")
        n = n.replace("c=", " ")
    elif "c-" in n:
        x += n.count("c-")
        n = n.replace("c-", " ")
    elif "dz=" in n:
        x += n.count("dz=")
        n = n.replace("dz=", " ")
    elif "d-" in n:
        x += n.count("d-")
        n = n.replace("d-", " ")
    elif "lj" in n:
        x += n.count("lj")
        n = n.replace("lj", " ")
    elif "nj" in n:
        x += n.count("nj")
        n = n.replace("nj", " ")
    elif "s=" in n:
        x += n.count("s=")
        n = n.replace("s=", " ")
    elif "z=" in n:
        x += n.count("z=")
        n = n.replace("z=", " ")
for i in range(27):
    if chr(97+i) in n:
        x += n.count(chr(97+i))
        n = n.replace(chr(97+i), " ")
print(x)
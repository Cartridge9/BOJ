a = int(input())
b = int(input())
c = int(input())
l = set([a, b, c])
if a+b+c != 180:
    print("Error")
elif len(l) == 3:
    print("Scalene")
elif len(l) == 2:
    print("Isosceles")
elif len(l) == 1:
    print("Equilateral")
    
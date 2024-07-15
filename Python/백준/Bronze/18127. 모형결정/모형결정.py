a, b = map(int, input().split())
A = 1
B = 1
x = a - 2
for i in range(b):
    B+=x
    A+=B
print(A)
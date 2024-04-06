a, b = map(list, input().split())
a.reverse()
b.reverse()
a = ''.join(a)
b = ''.join(b)
if a>b:
    print(a)
else:
    print(b)
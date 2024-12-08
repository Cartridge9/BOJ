a, b = list(map(int, input().split()))

n = 0
m = 0

n = int(-a+(a**2-b)**(1/2))
m = int(-a-(a**2-b)**(1/2))

numlist = set([n,m])

print(*sorted(numlist))
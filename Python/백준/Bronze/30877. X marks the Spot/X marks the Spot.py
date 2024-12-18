import sys
n = int(input())
result = ''
for i in range(n):
  a,b = map(str,sys.stdin.readline().split())
  a = a.lower()
  result += b[a.find('x')]
result = result.upper()
print(result)
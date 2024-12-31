import sys
input = sys.stdin.readline

def power(a,b):
    if b==0: return 1
    if b%2:
        return (power(a,b-1)*a) % 1000000007
    tmp=power(a,b//2) % 1000000007
    return tmp*tmp % 1000000007

for i in range(int(input())):
  a = int(input())
  if a == 1:
    print(5)
  else:
    print((4*power(5, a-1))%1000000007)
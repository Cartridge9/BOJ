n = list(input())
ans = []
c = 0
while(True):
  if len(n) < 2:
    n.append('0')
    n[0], n[1] = n[1], n[0]
  if len(ans) == 0:
    ans = [n[-1],str(sum(list(map(int, n))))[-1]]
  else:
    ans = [ans[-1], str(sum(list(map(int, ans))))[-1]]
  c+=1
  if ans == n: break
print(c)
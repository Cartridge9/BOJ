n = int(input())
a, b, c, d, e, f = list(map(int, input().split()))
if n == 1:
  print(a+b+c+d+e+f-max([a,b,c,d,e,f]))
else:
  paper = [[a, b, c], [a, d, e], [a, b, d], [a, e, c], [f, b, c], [f, d, e], [f, b, d], [f, e, c]]
  # print(paper)
  minpaper = [a, b, c]
  for i in paper:
    if sum(i) <= sum(minpaper):
      minpaper = i

  # print(minpaper)
  point = 8
  border = n-2
  inside = n**2-(point//2+border*4)

  result = 0
  minpaper.sort()
  # print(minpaper)
  result += sum(minpaper[0:3]) * point

  result += sum(minpaper[0:2]) * border * 3 * 4

  result += min(minpaper) * inside * 5

  result -= minpaper[2] * 4
  result -= minpaper[1] * (border * 4)

  print(result)

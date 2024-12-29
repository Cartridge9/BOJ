n = int(input())
a = input().split()
ad = dict()
max = 0

for i in a:
   if i not in ad:
      ad[i] = 1
   else:
      ad[i] += 1

      if ad[i] > 4:
         max = sum(list(ad.values()))
         break
      else:
         pass

print(max)
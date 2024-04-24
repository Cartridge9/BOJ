import math as m
a,b,v = map(int, input().split())
d = (v-b)/(a-b)
print(m.ceil(d))
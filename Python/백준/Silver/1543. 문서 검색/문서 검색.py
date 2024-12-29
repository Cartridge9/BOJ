t = input()
s = input()
t = t.replace(s, '0'*len(s)+'^')
print(t.count('^'))
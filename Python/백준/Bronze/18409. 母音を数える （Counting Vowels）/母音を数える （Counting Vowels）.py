l = ["a","i","e","o","u"]
n = int(input())
s = input()
c = 0
for i in range(n):
    if s[i] in l:
        c += 1
print(c)
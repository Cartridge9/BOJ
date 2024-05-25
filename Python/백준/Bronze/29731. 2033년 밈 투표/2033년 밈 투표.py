l = ["Never gonna give you up",
"Never gonna let you down"
,"Never gonna run around and desert you"
,"Never gonna make you cry"
,"Never gonna say goodbye"
,"Never gonna tell a lie and hurt you"
,"Never gonna stop"]
n = int(input())
cnt = 0
for i in range(n):
    a = input()
    if a in l:
        cnt += 1
    else:
        cnt -= 1
if cnt == n:
    print("No")
else:
    print("Yes")
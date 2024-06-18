num = int(input())
member = []
if num == 1:
    print(0)
else:
    for i in range(num):
        member.append(int(input()))
    i = 0
    members = list(reversed(sorted(member[1:])))
    while not member[0] > members[0]:
        i += 1
        members[0] -= 1
        member[0] += 1
        members = list(reversed(sorted(members)))
    print(i)
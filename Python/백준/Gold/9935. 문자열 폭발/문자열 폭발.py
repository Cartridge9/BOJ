a = list(input())
b = input()
l = len(b)
stack = []
for i in range(len(a)):
    stack.append(a[i])
    if "".join(stack[-l:]) == b:
        for j in range(l):
            # print(stack)
            stack.pop()
            # print("pop")
    # print(stack)
if not stack:
    print("FRULA")
else:
    print("".join(stack))
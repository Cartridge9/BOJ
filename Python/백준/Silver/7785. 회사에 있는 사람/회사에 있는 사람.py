n = int(input())
mem = dict()
for i in range(n):
  name, state = input().split()
  mem[name] = state

mem = [k for k, v in mem.items() if v == "enter"]
mem = sorted(mem, reverse=True)
print(*mem, sep='\n')
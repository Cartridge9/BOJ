cnt = 0
while True:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    cnt+=1
    print(f"Case {cnt}: Sorting... done!")
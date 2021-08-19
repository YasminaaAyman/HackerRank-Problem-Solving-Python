n = int(input().strip())
ar = list(map(int, input().rstrip().split()))

pair = 0
socks = set()
for i in range(len(ar)):
    if ar[i] not in socks:
        socks.add(ar[i])
    else:
        pair +=1
        socks.remove(ar[i])
print(pair)

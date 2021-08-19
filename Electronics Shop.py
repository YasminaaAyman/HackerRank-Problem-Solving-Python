b, n, m = map(int, input().split())
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))

most_expensive = -1

for i in range(len(keyboards)):
    for j in range(len(drives)):
        if most_expensive < keyboards[i]+drives[j] and keyboards[i]+drives[j] <= b:
            most_expensive = keyboards[i]+drives[j]
            
print(most_expensive)
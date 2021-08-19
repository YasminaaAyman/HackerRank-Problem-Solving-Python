n , k = map(int, input().split())
height = list(map(int, input().rstrip().split()))

if max(height) > k:
    print(max(height) - k)
else:
    print(0)
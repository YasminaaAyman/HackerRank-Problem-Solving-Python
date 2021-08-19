n, k = map(int, input().split())
c = list(map(int, input().rstrip().split()))

position = k % n
energy = 100 - 1 - c[position]*2
    
while position != 0:
    position = (position + k) % n
    energy -= 1 + c[position]*2

print(energy)
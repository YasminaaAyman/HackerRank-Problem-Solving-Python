q = int(input())

for _ in range(q):
    x, y, z = map(int, input().split())
    cat_a = abs(z - x)
    cat_b = abs(z - y)
    if cat_a < cat_b :
        print('Cat A')
    elif cat_b < cat_a:
        print('Cat B')
    elif cat_a == cat_b:
        print('Mouse C')
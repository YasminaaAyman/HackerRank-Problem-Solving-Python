steps = int(input().strip())
path = input()

level = 0
n = 0
for i in range(steps):
    if path[i] == 'D':
        level -= 1
        if level == -1 :
            n+=1
    elif path[i] == 'U':
        level += 1
        
print(n)
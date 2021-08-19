i, j, k = map(int, input().split())

coun_days = 0
for x in range(i,j+1):
    reversed_num = str(x)[::-1]
    calc_beautiful_day = abs(x-int(reversed_num)) % k
    if calc_beautiful_day == 0:
            coun_days += 1
        
print(coun_days)
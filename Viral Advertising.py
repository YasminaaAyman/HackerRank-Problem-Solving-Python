n = int(input().strip())
ads = 5
total_like = 0

for _ in range(n):
    people_like = ads//2
    total_like += people_like
    ads = people_like*3

print(total_like)
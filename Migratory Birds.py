
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    mig_birds = {}
    for i in range(len(arr)):
        if arr[i] not in mig_birds:
            mig_birds[arr[i]] = 1
        else:
            mig_birds[arr[i]] += 1
    max_value = max(mig_birds.values())
    bird_id = []
    for key,value in mig_birds.items():
        if value == max_value:
            bird_id.append(key)
    return min(bird_id)

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result) + '\n')


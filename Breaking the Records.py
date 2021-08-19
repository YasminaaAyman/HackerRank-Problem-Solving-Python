#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    high = scores[0]
    low = scores[0]
    count_max = count_min = 0
    for score in scores[1:]:
        if score > high:
            count_max += 1
            high = score
        if score < low:
            count_min += 1
            low = score
    return count_max, count_min
        

if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
    print('\n')


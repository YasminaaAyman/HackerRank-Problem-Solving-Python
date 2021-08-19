from collections import Counter

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a = Counter(a)
    maximum = 0
    for element in sorted(a):
        s = a[element] + a.get(element+1,0)
        if maximum < s:
            maximum = s
    return maximum

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(str(result) + '\n')


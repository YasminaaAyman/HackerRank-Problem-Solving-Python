#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    min_sum = arr[0]+arr[1]+arr[2]+arr[3]
    max_sum = arr[-1]+arr[-2]+arr[-3]+arr[-4]
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

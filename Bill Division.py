
#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    total_bill = sum(bill) - bill[k]
    actual_anna = total_bill//2
    return 'Bon Appetit' if actual_anna==b else (b-actual_anna)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    result = bonAppetit(bill, k, b)
    print(result)

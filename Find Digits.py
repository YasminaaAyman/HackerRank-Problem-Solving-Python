#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    count = 0
    for digit in n :
        if digit != '0' and int(n)%int(digit) == 0:
            count += 1

    return count

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = input().strip()

        result = findDigits(n)

        print(str(result))

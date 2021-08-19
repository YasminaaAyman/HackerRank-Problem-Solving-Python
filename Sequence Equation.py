#!/bin/python3
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    y=[]
    for number in range(1,len(p)+1):
        y.append(p.index(p.index(number)+1)+1)
    return y

if __name__ == '__main__':

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print('\n'.join(map(str, result)))


#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    count = 1
    for c in s :
        if c.isupper():
            count+=1
    return count

if __name__ == '__main__':
    s = input()

    result = camelcase(s)

    print(str(result) + '\n')


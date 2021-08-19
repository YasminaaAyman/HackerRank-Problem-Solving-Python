#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    if len(s) == 1:
        return s
    min_length = 1
    while min_length<len(s):
        if s[min_length] == s[min_length-1]:
            if len(s) == 2:
                return "Empty String"
            s = s[:min_length-1]+s[min_length+1:]
            min_length = 1
        else:
            min_length += 1
    if len(s) == 0:
        return "Empty String"
    else:
        return s
        

if __name__ == '__main__':
    s = input()

    result = superReducedString(s)

    print(result + '\n')


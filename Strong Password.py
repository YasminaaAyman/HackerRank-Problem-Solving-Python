#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def minimumNumber(n, password):
    required_chars = 0
    if not any(c in numbers for c in password):
        required_chars +=1
    if not any(c in lower_case for c in password):
        required_chars +=1
    if not any(c in upper_case for c in password):
        required_chars +=1
    if not any(c in special_characters for c in password):
        required_chars +=1
    if len(password) < 6:
        return max(required_chars, 6-len(password))
    return required_chars
    

if __name__ == '__main__':
    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    print(str(answer) + '\n')


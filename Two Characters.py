from itertools import combinations
import re

l = int(input().strip())
s = input()

word_len = 0
for c in combinations(set(s),2):
    two_char = "".join(c)
    option = re.sub("[^%s]"%two_char,"",s)
    if not re.search(r"(\w)\1", option) and len(option)>word_len:
        word_len = len(option)
print(word_len)
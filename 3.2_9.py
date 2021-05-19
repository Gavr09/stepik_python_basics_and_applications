# в каждой строке заменить все вхождения нескольких одинаковых букв (символы из \w) на одну букву
'''
Input:
attraction
buzzzzz

Output:
atraction
buz
'''

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(\w)\1+'
    # print(r'\1')
    # print(line)
    # print(re.findall(pattern, line))
    print(re.sub(pattern, r'\1', line))

# в каждой строке заменить первое вхождение слова, состоящего только из латинских букв a (регистр не важен),
# на слово argh
'''
Input:
sdasdas
There'll be no more 'Aaaaaaaaaaa'
AaAaAaA AaAaAaA

Output:
sdasdas
There'll be no more 'argh'
argh AaAaAaA
'''

import sys
import re

# pattern = r'([\b\'\"])[a, A]+\1'
for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(\b)[aA]+(\b)'
    # print(r'\1')
    # print(line)
    # print(re.findall(pattern, line))
    print(re.sub(pattern, r'\1argh\2', line, 1))

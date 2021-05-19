# в каждой строке поменять местаме две первых буквы (символ из \w) в каждом слове, состоящем хотя бы из двух букв
'''
Input:
this is a text
"this' !is. &n1ce,

Output:
htis si a etxt
"htis' !si. &1nce,
'''

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(\b)(\w)(\w)(\w*)(\b)'
    # print(r'\1')
    # print(line)
    # print(re.findall(pattern, line))
    print(re.sub(pattern, r'\1\3\2\4\5', line))

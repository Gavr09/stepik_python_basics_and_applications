# вывести строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор)
'''
Input:
blabla is a tandem repetition
123123 is good too
go go
aaa

Output:
blabla is a tandem repetition
123123 is good too
'''

import sys
import re

pattern = r'\b(\S+)\1\b'
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) > 0:
        # print(re.match(pattern, line))
        print(line)
